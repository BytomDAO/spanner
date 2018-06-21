import json
import os
import time

from Account import Account
from Asset import Asset
from Transaction import Action, Transaction


class UnspentOutputs(object):

    @staticmethod
    def get_block_height(connection):
        response = connection.request("/get-block-count")

        resp_json = json.loads(response.text)

        if resp_json['status'] == 'success':
            return resp_json['data']['block_count'], 1
        elif resp_json['status'] == 'fail':
            return resp_json['msg'], -1
        else:
            return resp_json, 0

    @staticmethod
    def list_UTXO(connection):
        response = connection.request("/list-unspent-outputs")

        resp_json = json.loads(response.text)

        if resp_json['status'] == 'success':
            return resp_json['data'], 1
        elif resp_json['status'] == 'fail':
            return resp_json['msg'], -1
        else:
            return resp_json, 0

    @staticmethod
    def list_mature_UTXO(connection):
        result = []
        utxos, ret = UnspentOutputs.list_UTXO(connection=connection)
        block_height, ret_code = UnspentOutputs.get_block_height(connection=connection)
        if ret == 1 and ret_code == 1:
            for utxo in utxos:
                # append mature utxo to set
                if utxo['valid_height'] < block_height:
                    result.append(utxo)
        return result

    @staticmethod
    def list_by_account_asset(connection, account_alias, asset_alias):
        utxos = UnspentOutputs.list_mature_UTXO(connection)
        result = []
        for utxo in utxos:
            if utxo['account_alias'] == account_alias and utxo['asset_alias'] == asset_alias:
                result.append(utxo)

        return result

    @staticmethod
    def find_little_utxo(max_amount=5000000000, utxos=[]):
        result = []
        for utxo in utxos:
            if utxo['amount'] <= max_amount:
                result.append(utxo)
        return result

    @staticmethod
    def combine_actions(connection, account_alias, asset_alias, max_amount=5000000000, size=20):
        actions = []
        gas_amount = 40000000
        amount = 0
        asset = Asset.get_asset_by_alias(connection, asset_alias)
        asset_id = asset['id']
        address = Account.find_address_by_alias(connection, account_alias)

        result = UnspentOutputs.list_by_account_asset(connection, account_alias, asset_alias)
        utxos = UnspentOutputs.find_little_utxo(max_amount=max_amount, utxos=result);

        if utxos.__len__() <= size:
            for utxo in utxos:
                actions.append(Action.unspent_output(output_id=utxo['id']))
                amount = amount + utxo['amount']
        else:
            for i in range(0, size):
                actions.append(Action.unspent_output(output_id=utxos[i]['id']))
                amount = amount + utxos[i]['amount']

        # consider gas amount
        if amount > gas_amount:
            amount = amount - gas_amount
        else:
            print('\nAttention: The amount of all utxos is too little, less than tx gas.')
            os._exit(0)
        actions.append(Action.control_address(amount=amount, asset_id=asset_id, address=address))

        return actions

    @staticmethod
    def combine_utxos(connection, account_alias, password, asset_alias='BTM', max_amount=5000000000, size=20):
        actions = UnspentOutputs.combine_actions(connection, account_alias, asset_alias, max_amount, size)
        # print(actions)
        issuance = Transaction.build_transaction(connection, actions)
        # print("issuance:", issuance)
        # sign transaction
        signed_raw_transaction = Transaction.sign_transaction(connection, password, issuance)
        # print("signed_raw_transaction:", signed_raw_transaction)
        # submit transaction
        tx_submit = Transaction.submit_transaction(connection, signed_raw_transaction)
        tx_id = tx_submit['tx_id']
        print("tx_id:", tx_id)
        if tx_id is not None:
            print("success to combine utxos.")

            print("wait combine tx to chain...(about 2.5 minutes)")

            while True:
                tx, ret = Transaction.get_transaction(connection=connection, tx_id=tx_id)
                if ret == 1:
                    # print(tx)
                    if int(tx['block_index']) > 0:
                        print("combine tx to chain. You can combine next utxos.")
                        break
                elif ret == -1:
                    print("tx:", tx)
                    break
                time.sleep(2)
        else:
            print(actions)
            print("issuance:", issuance)
            print("signed_raw_transaction:", signed_raw_transaction)

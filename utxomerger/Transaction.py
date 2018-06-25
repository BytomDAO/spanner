import json

from Account import Account


class Transaction(object):

    @staticmethod
    def list_transactions(connection):
        response = connection.request("/list-transactions")

        resp_json = json.loads(response.text)

        if resp_json['status'] == 'success':
            return resp_json['data']
        elif resp_json['status'] == 'fail':
            return resp_json['msg']
        else:
            return resp_json

    @staticmethod
    def list_by_account_id(connection, account_id):
        body_json = {"account_id": account_id}
        response = connection.request("/list-transactions", body_json)

        resp_json = json.loads(response.text)

        if resp_json['status'] == 'success':
            return resp_json['data']
        elif resp_json['status'] == 'fail':
            return resp_json['msg']
        else:
            return resp_json

    @staticmethod
    def list_by_account_alias(connection, account_alias):
        account = Account.find_by_alias(connection, account_alias)
        body_json = {"account_id": account.id}
        response = connection.request("/list-transactions", body_json)

        resp_json = json.loads(response.text)

        if resp_json['status'] == 'success':
            return resp_json['data']
        elif resp_json['status'] == 'fail':
            return resp_json['msg']
        else:
            return resp_json

    @staticmethod
    def get_transaction(connection, tx_id):
        body_json = {"tx_id": tx_id}
        response = connection.request("/get-transaction", body_json)

        resp_json = json.loads(response.text)

        if resp_json['status'] == 'success':
            return resp_json['data'], 1
        elif resp_json['status'] == 'fail':
            return resp_json['msg'], -1
        else:
            return resp_json, 0

    @staticmethod
    def build_transaction(connection, actions):
        # ttl: 15min=900000ms
        body_json = {"base_transaction": None, "actions": actions,
                     "ttl": 1, "time_range": 0}
        response = connection.request("/build-transaction", body_json)

        resp_json = json.loads(response.text)

        if resp_json['status'] == 'success':
            return resp_json['data']
        elif resp_json['status'] == 'fail':
            return resp_json['msg']
        else:
            return resp_json

    @staticmethod
    def sign_transaction(connection, password, transaction):
        body_json = {"password": password, "transaction": transaction}
        response = connection.request("/sign-transaction", body_json)

        resp_json = json.loads(response.text)

        if resp_json['status'] == 'success':
            return resp_json['data']
        elif resp_json['status'] == 'fail':
            return resp_json['msg']
        else:
            return resp_json

    @staticmethod
    def submit_transaction(connection, raw_transaction):
        body_json = {"raw_transaction": raw_transaction}
        response = connection.request("/submit-transaction", body_json)

        resp_json = json.loads(response.text)

        if resp_json['status'] == 'success':
            return resp_json['data']


class Action(object):

    @staticmethod
    def spend_account(amount, account_id, asset_id):
        return {
            'amount': amount,
            'account_id': account_id,
            'asset_id': asset_id,
            'type': 'spend_account'
        }

    @staticmethod
    def issue(amount, asset_id):
        return {
            'amount': amount,
            'asset_id': asset_id,
            'type': 'issue'
        }

    @staticmethod
    def gas(amount, account_id, asset_id):
        return {
            'amount': amount,
            'account_id': account_id,
            'asset_id': asset_id,
            'type': 'spend_account'
        }

    @staticmethod
    def control_address(amount, asset_id, address):
        return {
            'amount': amount,
            'asset_id': asset_id,
            'address': address,
            'type': 'control_address'
        }

    @staticmethod
    def unspent_output(output_id):
        return {
            'type': 'spend_account_unspent_output',
            'output_id': output_id
        }

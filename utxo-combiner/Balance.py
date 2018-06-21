import json


class Balance(object):

    @staticmethod
    def list(connection):
        response = connection.request("/list-balances")

        resp_json = json.loads(response.text)

        if resp_json['status'] == 'success':
            return resp_json['data']
        elif resp_json['status'] == 'fail':
            return resp_json['msg']
        else:
            return resp_json

    @staticmethod
    def get_by_account_alias(connection, account_alias):
        balance_list = Balance.list(connection)
        account_balances = []
        for balance in balance_list:
            if balance['account_alias'] == account_alias:
                account_balances.append(balance)

        return account_balances

    @staticmethod
    def get_by_asset_alias(connection, asset_alias):
        balance_list = Balance.list(connection)
        asset_balances = []
        for balance in balance_list:
            if balance['asset_alias'] == asset_alias.upper():
                asset_balances.append(balance)

        return asset_balances

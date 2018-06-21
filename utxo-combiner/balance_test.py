import unittest

from Account import Account
from Asset import Asset
from Balance import Balance
from connection import Connection
from keys import Keys


class TestAssetMethods(unittest.TestCase):

    def test_list(self):
        con = Connection("http://127.0.0.1:9888")
        balance_list = Balance.list(con)
        for balance in balance_list:
            print(str(balance))

    def test_get_by_account_alias(self):
        con = Connection("http://127.0.0.1:9888")
        account_alias = 'test'
        balance = Balance.get_by_account_alias(con, account_alias)
        print(balance)
        print(balance.__len__())

    def test_get_by_asset_alias(self):
        con = Connection("http://127.0.0.1:9888")
        balance = Balance.get_by_asset_alias(con, 'btm')
        print(balance)
        print(balance.__len__())

    def test_create(self):
        con = Connection("http://127.0.0.1:9888")
        xpub = Keys.find_by_alias(con, "sheng").xpub
        asset = Asset.create(con, [xpub], "shengsheng", 1)
        print(asset.id)

    def test_update_alias(self):
        con = Connection("http://127.0.0.1:9888")
        response = Asset.update_alias(con, "d05b4cc1615509bf0d58cda7be4c5da43a33cc920ae439eaaac6507853e3cbf1", "shengsheng")
        print(response)

    if __name__ == '__main__':
        unittest.main()

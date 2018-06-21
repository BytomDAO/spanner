import unittest

from Transaction import Transaction
from connection import Connection
from UnspentOutputs import UnspentOutputs


class TestUTXOMethods(unittest.TestCase):

    def test_list_UTXO(self):
        con = Connection("http://127.0.0.1:9888")
        utxos, ret = UnspentOutputs.list_UTXO(con)
        if ret == 1:
            for utxo in utxos:
                print(utxo)

    def test_list_by_account_asset(self):
        con = Connection("http://127.0.0.1:9888")
        account_alias = "zhangsan"
        asset_alias = "BTM"
        utxos = UnspentOutputs.list_by_account_asset(con, account_alias, asset_alias)
        for utxo in utxos:
            if utxo['amount'] < 41250000000:
                print(utxo)

    def test_find_little_utxo(self):
        con = Connection("http://127.0.0.1:9888")
        account_alias = "zhangsan"
        asset_alias = "BTM"
        utxos = UnspentOutputs.list_by_account_asset(con, account_alias, asset_alias)
        result = UnspentOutputs.find_little_utxo(max_amount=5000000000, utxos=utxos)
        print(result.__len__())
        for utxo in result:
            print(utxo)

    def test_combine_actions(self):
        con = Connection("http://127.0.0.1:9888")
        account_alias = "zhangsan"
        asset_alias = "BTM"
        actions = UnspentOutputs.combine_actions(con, account_alias, asset_alias)
        print("action begin")
        for action in actions:
            print(action)
        print("action end")

    def test_combine_utxos(self):
        con = Connection("http://127.0.0.1:9888")
        account_alias = "zhangsan"
        asset_alias = "BTM"
        UnspentOutputs.combine_utxos(connection=con, account_alias=account_alias, password='123456', max_amount=5000000000, size=20)

    if __name__ == '__main__':
        unittest.main()

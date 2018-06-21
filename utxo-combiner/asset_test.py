import unittest

from Account import Account
from Asset import Asset
from connection import Connection
from keys import Keys


class TestAssetMethods(unittest.TestCase):

    def test_list(self):
        con = Connection("http://127.0.0.1:9888")
        asset_list = Asset.list(con)
        for asset in asset_list:
            print(str(asset))

    def test_get_asset(self):
        con = Connection("http://127.0.0.1:9888")
        asset_id = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
        asset = Asset.get_asset(con, asset_id)
        print(asset)

    def test_get_by_alias(self):
        con = Connection("http://127.0.0.1:9888")
        asset = Asset.get_asset_by_alias(con, "gold")
        print(asset)

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

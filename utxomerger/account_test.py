import unittest

from Account import Account
from connection import Connection
from keys import Keys


class TestAccountMethods(unittest.TestCase):

    def test_list(self):
        con = Connection("http://127.0.0.1:9888")
        account_list = Account.list(con)
        for account in account_list:
            print(account.id, account.alias, account.xpubs, account.key_index, account.quorum)
        self.assertIsNotNone(account_list)

    def test_find_by_alias(self):
        con = Connection("http://127.0.0.1:9888")
        account = Account.find_by_alias(con, "receiver-account")
        print(account.id, account.alias, account.xpubs, account.key_index, account.quorum)

    def test_create(self):
        con = Connection("http://127.0.0.1:9888")
        xpub = Keys.find_by_alias(con, "test").xpub
        account = Account.create(con, [xpub], "shengsheng", 1)
        print(account.id, account.alias, account.xpubs, account.key_index, account.quorum)

    def test_delete(self):
        con = Connection("http://127.0.0.1:9888")
        status = Account.delete(con, "shengsheng")
        self.assertIs("true", status)

    def test_create_address(self):
        con = Connection("http://127.0.0.1:9888")
        account = Account.find_by_alias(con, "zhangsan")

        response = Account.create_address(con, "zhangsan", account.id)
        print(response)
        print(response['address'])

    if __name__ == '__main__':
        unittest.main()

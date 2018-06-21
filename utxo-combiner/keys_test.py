import unittest

from connection import Connection
from keys import Keys


class TestKeysMethods(unittest.TestCase):

    def test_list(self):
        con = Connection("http://127.0.0.1:9888")
        key_list = Keys.list(con)
        for key in key_list:
            print(key.alias, key.xpub, key.file)
        self.assertIsNotNone(key_list)

    def test_find_by_alias(self):
        con = Connection("http://127.0.0.1:9888")
        key = Keys.find_by_alias(con, "sender-key")
        print(key.alias, key.xpub, key.file)
        self.assertIsNotNone(key)

    def test_create(self):
        con = Connection("http://127.0.0.1:9888")
        key = Keys.create(con, "sheng", "123456")
        print(key.alias, key.xpub, key.file)
        self.assertIsNotNone(key)

    def test_delete(self):
        con = Connection("http://127.0.0.1:9888")
        xpub = Keys.find_by_alias(con, "sheng").xpub
        status = Keys.delete(con, xpub, "123456")
        self.assertIs("true", status)
        pass

    def test_delete_by_alias(self):
        con = Connection("http://127.0.0.1:9888")
        status = Keys.delete_by_alias(con, "sheng", "123456")
        self.assertIs("true", status)

    def test_reset_password(self):
        con = Connection("http://127.0.0.1:9888")
        xpub = Keys.find_by_alias(con, "sheng").xpub
        print(xpub)
        status = Keys.reset_password(con, xpub, "567890", "123456")
        self.assertIs("true", status)

    if __name__ == '__main__':
        unittest.main()

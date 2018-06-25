import unittest

from Transaction import Transaction
from connection import Connection
from UnspentOutputs import UnspentOutputs


class TestUTXOMethods(unittest.TestCase):

    def test_get_block_height(self):
        con = Connection("http://127.0.0.1:9888")
        block_height, ret = UnspentOutputs.get_block_height(connection=con)
        if ret == 1:
            print(block_height)

    def test_list_UTXO(self):
        con = Connection("http://127.0.0.1:9888")
        utxos, ret = UnspentOutputs.list_UTXO(con)
        if ret == 1:
            for utxo in utxos:
                print(utxo)

    if __name__ == '__main__':
        unittest.main()

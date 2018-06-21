import unittest

from Transaction import Transaction, Action
from connection import Connection


class TestTransactionMethods(unittest.TestCase):

    def test_list_transactions(self):
        con = Connection("http://127.0.0.1:9888")
        transactions = Transaction.list_transactions(con)
        for tx in transactions:
            print(tx)

    def test_list_by_account_id(self):
        con = Connection("http://127.0.0.1:9888")
        account_id = "0E6KP8C100A02"
        transactions = Transaction.list_by_account_id(con, account_id)
        for tx in transactions:
            print(tx)

    def test_list_by_account_alias(self):
        con = Connection("http://127.0.0.1:9888")
        account_alias = "receiver-account"
        transactions = Transaction.list_by_account_alias(con, account_alias)
        for tx in transactions:
            print(tx)

    def test_get_transaction(self):
        con = Connection("http://127.0.0.1:9888")
        tx_id = "5120dc0b2fe372e8f551b7e02ce5a44eb2a7b37108303d15ef8b601bfc9c1d5b"
        tx = Transaction.get_transaction(con, tx_id)
        print(tx)

    def test_issue_transaction(self):
        # build transaction
        con = Connection("http://127.0.0.1:9888")
        asset_id = 'd2d938352d324e68c21b3c8b3a7f8587f237d100cd5618cc0ba3ba35bbb7185d'
        account_id = '0E6K7AFF00A02'
        btm_id = 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
        address = 'sm1qz2j8k5anh0d0nu63pcwccxwkn7qu4y2zjwaj5h'
        actions = [
            Action.issue(10000, asset_id),
            Action.gas(20000000, account_id, btm_id),
            Action.control_address(10000, asset_id, address)
        ]
        print(actions)
        issuance = Transaction.build_transaction(con, actions)
        print("issuance:", issuance)
        # sign transaction
        signed_raw_transaction = Transaction.sign_transaction(con, '123456', issuance)
        print("signed_raw_transaction:", signed_raw_transaction)
        # submit transaction
        tx_id = Transaction.submit_transaction(con, signed_raw_transaction)
        print("tx_id:", tx_id)

    def test_spend_transaction(self):
        # build transaction
        con = Connection("http://127.0.0.1:9888")
        asset_id = 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
        account_id = '0F87NG1800A02'
        btm_id = 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
        address = 'sm1qvyus3s5d7jv782syuqe3qrh65fx23lgpzf33em'
        actions = [
            Action.spend_account(125000000000, account_id, asset_id),
            Action.gas(40000000, account_id, btm_id),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
            Action.control_address(5000000000, asset_id, address),
        ]
        print(actions)
        issuance = Transaction.build_transaction(con, actions)
        print("issuance:", issuance)
        # sign transaction
        signed_raw_transaction = Transaction.sign_transaction(con, '123456', issuance)
        print("signed_raw_transaction:", signed_raw_transaction)
        # submit transaction
        tx_id = Transaction.submit_transaction(con, signed_raw_transaction)
        print("tx_id:", tx_id)

    if __name__ == '__main__':
        unittest.main()

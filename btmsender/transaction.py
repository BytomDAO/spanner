import os
import sys
from . import httprequest


class BTMSender:
    miner_fee = 40000000
    max_output_count = 1500

    def __init__(self, _node_address, _input_path, _account_id, _password, _output_count, _use_unconfirmed,
                 _time_range):
        self.node_address = _node_address
        self.input_path = _input_path
        self.account_id = _account_id
        self.password = _password
        self.output_count = _output_count
        self.use_unconfirmed = _use_unconfirmed
        self.time_range = _time_range

    def handle_input(self):
        if self.output_count <= 0:
            self.output_count = self.max_output_count
        lines = list()
        with open(self.input_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if len(lines) < self.output_count:
                    lines.append(line)
                else:
                    self.handle_transaction(lines)
                    lines.clear()
                    lines.append(line)
        if len(lines) > 0:
            self.handle_transaction(lines)
        print('Transactions are completed.Please check completed.txt')

    def handle_transaction(self, lines):
        data = self.build_transaction(lines)
        data = self.sign_transaction(data)
        if data['sign_complete']:
            data = self.submit_transaction(data)
            tx_id = data['tx_id']
            if tx_id:
                print('transaction_id:\n' + tx_id)
                write_lines_to_file(lines, self.input_path)
        else:
            print('Sign transaction is failed.Please check account password.')
            sys.exit(1)

    # parameter lines: max_output line list
    def build_transaction(self, _lines):
        amount_sum = 0
        action_list = list()
        for line in _lines:
            data = line.strip().split(',')
            address = data[0]
            amount = int(data[1])
            amount_sum += amount
            address_dict = get_address_dict(amount, address)
            action_list.append(address_dict)
        amount_sum += self.miner_fee
        spend_dict = get_spend_dict(self.account_id, int(amount_sum), self.use_unconfirmed)
        action_list.insert(0, spend_dict)
        parameter = {'base_transaction': None, 'actions': action_list, 'ttl': 0}
        if self.time_range != 0:
            parameter.update(time_range=self.time_range)
        return httprequest.post(self.node_address, 'build-transaction', parameter)

    # parameter transaction: dict from build_transaction function return
    def sign_transaction(self, _transaction):
        parameter = {'password': self.password, 'transaction': _transaction}
        return httprequest.post(self.node_address, 'sign-transaction', parameter)

    def submit_transaction(self, _transaction):
        parameter = {'raw_transaction': _transaction['transaction']['raw_transaction']}
        return httprequest.post(self.node_address, 'submit-transaction', parameter)


# write complete transactions lines to file
def write_lines_to_file(lines, _path):
    _path = os.path.abspath(os.path.dirname(_path)) + os.path.sep + 'completed.txt'
    with open(_path, 'a', encoding='utf-8') as file:
        file.write('\n'.join(lines) + '\n\n')


# control_address action
def get_address_dict(_amount, _address):
    return {'amount': _amount,
            'asset_id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff',
            'address': _address,
            'type': 'control_address'}


# spend_account action
def get_spend_dict(_account_id, _amount_sum, _use_unconfirmed):
    return {'account_id': _account_id,
            'amount': _amount_sum,
            'asset_id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff',
            'type': 'spend_account',
            'use_unconfirmed': _use_unconfirmed}

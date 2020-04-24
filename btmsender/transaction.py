import os
import sys

from . import const
from . import httprequest


class BTMSender:
    def __init__(self, _input):
        self.input = _input

    def handle_input(self):
        if self.input.output_count <= 0:
            self.input.output_count = const.max_output_count
        lines = list()
        with open(self.input.input_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if len(lines) < self.input.output_count:
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
                write_lines_to_file(lines, self.input.input_path)
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
            address_dict = self.get_address_dict(amount, address)
            action_list.append(address_dict)
        fee_dict = self.get_spend_dict(const.miner_fee, const.btm_asset_id)
        spend_dict = self.get_spend_dict(int(amount_sum), self.input.asset_id)
        action_list.insert(0, spend_dict)
        action_list.insert(1, fee_dict)
        parameter = {'base_transaction': None, 'actions': action_list, 'ttl': 0}
        if self.input.time_range != 0:
            parameter.update(time_range=self.input.time_range)
        return httprequest.post(self.input.node_address, 'build-transaction', parameter)

    # parameter transaction: dict from build_transaction function return
    def sign_transaction(self, _transaction):
        parameter = {'password': self.input.password, 'transaction': _transaction}
        return httprequest.post(self.input.node_address, 'sign-transaction', parameter)

    def submit_transaction(self, _transaction):
        parameter = {'raw_transaction': _transaction['transaction']['raw_transaction']}
        return httprequest.post(self.input.node_address, 'submit-transaction', parameter)

    # control_address action
    def get_address_dict(self, _amount, _address):
        return {'amount': _amount,
                'asset_id': self.input.asset_id,
                'address': _address,
                'type': 'control_address'}

    # spend_account action
    def get_spend_dict(self, _amount_sum, _asset_id):
        return {'account_id': self.input.account_id,
                'amount': _amount_sum,
                'asset_id': _asset_id,
                'type': 'spend_account',
                'use_unconfirmed': self.input.use_unconfirmed}


# write complete transactions lines to file
def write_lines_to_file(lines, _path):
    _path = os.path.abspath(os.path.dirname(_path)) + os.path.sep + 'completed.txt'
    with open(_path, 'a', encoding='utf-8') as file:
        file.write('\n'.join(lines) + '\n\n')

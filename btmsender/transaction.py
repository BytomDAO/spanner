import os
import sys
from . import httprequest

miner_fee = 40000000
max_output_count = 1500


def handle_input(_path, _account_id, _password, _output_count, _use_unconfirmed, _time_range):
    if _output_count <= 0:
        _output_count = max_output_count
    lines = list()
    with open(_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if len(lines) < _output_count:
                lines.append(line)
            else:
                handle_transaction(lines, _path, _account_id, _password, _use_unconfirmed, _time_range)
                lines.clear()
                lines.append(line)
    if len(lines) > 0:
        handle_transaction(lines, _path, _account_id, _password, _use_unconfirmed, _time_range)
    print('Transactions are completed.Please check completed.txt')


def handle_transaction(lines, _path, _account_id, _password, _use_unconfirmed, _time_range):
    data = build_transaction(lines, _account_id, _use_unconfirmed, _time_range)
    data = sign_transaction(_password, data)
    if data['sign_complete']:
        data = submit_transaction(data)
        txid = data['tx_id']
        if txid:
            print('transaction_id:\n' + txid)
            write_lines_to_file(lines, _path)
    else:
        print('Sign transaction is failed.Please check account password.')
        sys.exit(1)


# parameter lines: max_output line list
def build_transaction(_lines, _account_id, _use_unconfirmed, _time_range):
    amount_sum = 0
    action_list = list()
    for line in _lines:
        data = line.strip().split(',')
        address = data[0]
        amount = int(data[1])
        amount_sum += amount
        address_dict = get_address_dict(amount, address)
        action_list.append(address_dict)
    amount_sum += miner_fee
    spend_dict = get_spend_dict(_account_id, int(amount_sum), _use_unconfirmed)
    action_list.insert(0, spend_dict)
    parameter = {'base_transaction': None, 'actions': action_list, 'ttl': 0}
    if _time_range != 0:
        parameter.update(time_range=_time_range)
    return httprequest.post('build-transaction', parameter)


# parameter transaction: dict from build_transaction function return
def sign_transaction(_password, _transaction):
    parameter = {'password': _password, 'transaction': _transaction}
    return httprequest.post('sign-transaction', parameter)


def submit_transaction(_transaction):
    parameter = {'raw_transaction': _transaction['transaction']['raw_transaction']}
    return httprequest.post('submit-transaction', parameter)


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

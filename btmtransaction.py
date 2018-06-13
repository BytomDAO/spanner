import os
import sys
import httprequest

miner_fee = 40000000
max_output = 100


def handle_input(_path, _account_id, _password):
    lines = list()
    with open(_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if len(lines) < max_output:
                lines.append(line)
            else:
                handle_transaction(lines, _path, _account_id, _password)
                lines.clear()
                lines.append(line)
    if len(lines) > 0:
        handle_transaction(lines, _path, _account_id, _password)
    print('Transaction is accomplished.Please check accomplished.txt')


def handle_transaction(lines, _path, _account_id, _password):
    data = build_transaction(lines, _account_id)
    data = sign_transaction(_password, data)
    if data['sign_complete']:
        data = submit_transaction(data)
        txid = data['tx_id']
        if txid:
            print('transaction_id:\n' + txid)
            lines = append_txid_to_lines(lines, txid)
            write_lines_to_file(lines, _path)
    else:
        print('Sign transaction is failed.Please check account password.')
        sys.exit(1)


# parameter lines: max_output line list
def build_transaction(_lines, _account_id):
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
    spend_dict = get_spend_dict(_account_id, int(amount_sum))
    action_list.insert(0, spend_dict)
    parameter = {'base_transaction': None, 'actions': action_list, 'ttl': 0}
    return httprequest.post('build-transaction', parameter)


# parameter transaction: dict from build_transaction function return
def sign_transaction(_password, _transaction):
    parameter = {'password': _password, 'transaction': _transaction}
    return httprequest.post('sign-transaction', parameter)


def submit_transaction(_transaction):
    parameter = {'raw_transaction': _transaction['transaction']['raw_transaction']}
    return httprequest.post('submit-transaction', parameter)


def append_txid_to_lines(lines, txid):
    for i in range(len(lines)):
        # lines[i] = lines[i] + ',' + txid + '\n'
        lines[i] = lines[i] + ',' + '\n'
    return lines


# write complete transactions lines to file
def write_lines_to_file(lines, _path):
    _path = os.path.abspath(os.path.dirname(_path)) + os.path.sep + 'accomplished.txt'
    with open(_path, 'a', encoding='utf-8') as file:
        file.writelines(lines)


# control_address action
def get_address_dict(_amount, _address):
    return {'amount': _amount,
            'asset_id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff',
            'address': _address,
            'type': 'control_address'}


# spend_account action
def get_spend_dict(_account_id, _amount_sum):
    return {'account_id': _account_id,
            'amount': _amount_sum,
            'asset_id': 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff',
            'type': 'spend_account'}

# if __name__ == "__main__":
#     path = '/Users/john/Desktop/btm.txt'
#     account_id = '0F0BV1OLG0A04'
#     password = '123456'
#     sys.exit(handle_input(path, account_id, password))

import os
import sys
import argparse

from . import const
from . import httprequest


class Input:
    def __init__(self, node_address, input_path, account_id, asset_id, password, output_count, use_unconfirmed,
                 time_range):
        self.node_address = node_address
        self.input_path = input_path
        self.account_id = account_id
        self.asset_id = asset_id
        self.password = password
        self.output_count = output_count
        self.use_unconfirmed = use_unconfirmed
        self.time_range = time_range


def validate_address(node_address, line, address):
    parameter = {'address': address}
    data = httprequest.post(node_address, 'validate-address', parameter)
    if not data['valid']:
        print(line + 'This line transaction address is not valid')
        sys.exit(1)


def validate_amount(line, amount):
    try:
        int(amount)
    except ValueError:
        print(line + 'This line transaction amount is not int.')
        sys.exit(1)


def get_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', required=True, help='bytomd or vapord node api address')
    parser.add_argument('-i', required=True, help='transaction input file')
    parser.add_argument('-a', required=True, help='wallet account id')
    parser.add_argument('-s', type=str, default=const.btm_asset_id, help='transaction asset id')
    parser.add_argument('-c', type=int, default=0, help='transaction max output count')
    parser.add_argument('-u', action='store_true', help='use unconfirmed UTXO build transaction')
    parser.add_argument('-t', type=int, default=0,
                        help='the transaction will not be submitted into block after this height')
    args = parser.parse_args()
    _input = Input(node_address=args.n, input_path=args.i, account_id=args.a, asset_id=args.s, password="",
                   output_count=args.c, use_unconfirmed=args.u, time_range=args.t)
    return _input


def validate_input():
    _input = get_input()
    # relative path
    file_path = os.path.abspath('.') + os.path.sep + _input.input_path
    if not os.path.exists(file_path):
        # absolute path
        file_path = _input.input_path
    total_amount = 0
    # read file
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            splits = line.strip().split(',')
            validate_address(_input.node_address, line, splits[0])
            validate_amount(line, splits[1])
            total_amount += int(splits[1])

    if _input.asset_id == const.btm_asset_id:
        print('Transactions address and amount are valid.' +
              '\nTotal amount is %.2f BTM(without gas).' % (total_amount / pow(10, 8)))
    else:
        print('Transactions address and amount are valid.' +
              '\nTotal amount is {total_amount} {asset_id}.'
              .format(total_amount=total_amount, asset_id=_input.asset_id))

    password = input("Please input your account password:")
    _input.input_path = file_path
    _input.password = password
    return _input

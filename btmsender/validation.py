import os
import sys
import argparse
from . import httprequest


def validate_address(line, address):
    parameter = {'address': address}
    data = httprequest.post('validate-address', parameter)
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
    parser.add_argument('-i', required=True, help='transaction input file')
    parser.add_argument('-a', required=True, help='wallet account id')
    parser.add_argument('-p', required=True, help='wallet account password')
    parser.add_argument('-c', type=int, default=0, help='transaction max output count')
    parser.add_argument('-u', action='store_true', help='use unconfirmed UTXO build transaction')
    parser.add_argument('-t', type=int, default=0,
                        help='the transaction will not be submitted into block after this height')
    args = parser.parse_args()
    return args.i, args.a, args.p, args.c, args.u, args.t


def validate_input():
    input_path, account_id, password, output_count, use_unconfirmed, time_range = get_input()
    # relative path
    file_path = os.path.abspath('.') + os.path.sep + input_path
    if not os.path.exists(file_path):
        # absolute path
        file_path = input_path
    total_amount = 0
    # read file
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            splits = line.strip().split(',')
            validate_address(line, splits[0])
            validate_amount(line, splits[1])
            total_amount += int(splits[1])
    print('Transactions address and amount are valid.' +
          '\nTotal amount is %.2f BTM(without gas).Send BTM or not?(y/n)' % (total_amount / pow(10, 8)))
    if input() != 'y':
        sys.exit(0)
    return file_path, account_id, password, output_count, use_unconfirmed, time_range

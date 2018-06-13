#!/usr/bin/env python3

import os
import sys
import getopt
import httprequest


def validate_address(line, address):
    parameter = {'address': address}
    data = httprequest.post('validate-address', parameter)
    if not data['valid']:
        print(line + 'This line transaction address is not validate')
        sys.exit(1)


def validate_amount(line, amount):
    try:
        int(amount)
    except ValueError:
        print(line + 'This line transaction amount is not int.')
        sys.exit(1)


def validate_input(argv):
    global input_path
    global account_id
    try:
        opts, args = getopt.getopt(argv[1:], 'a:i:', ['account=', 'input='])
        if len(opts) < 2:
            raise getopt.GetoptError('lose command option parameter')
    except getopt.GetoptError as err:
        print('Input error:' + str(err) +
              '\n' + 'Example usage:' +
              '\n' + '\t./btmtransfer.py -i input.txt -a 0BF63M2U00A04')
        sys.exit(1)
    for opt, arg in opts:
        if opt in ('-a', '--account'):
            account_id = arg
        if opt in ('-i', '--input'):
            input_path = arg
    # relative path
    path = os.path.abspath('.') + '/' + input_path
    if not os.path.exists(path):
        # absolute path
        path = input_path
    # read file
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            splits = line.strip().split(',')
            validate_address(line, splits[0])
            validate_amount(line, splits[1])


def main(argv=None):
    if argv is None:
        argv = sys.argv
    validate_input(argv)


if __name__ == "__main__":
    sys.exit(main())

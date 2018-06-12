#!/usr/bin/env python3

import os
import sys
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
    if len(argv) < 2 or len(argv) >= 2 and not str(argv[1]).endswith('.txt'):
        print('Input error:Use this script with input txt file.'
              + '\n' + 'Example usage:' + '\n' + '\t./btmtransfer.py input.txt')
        sys.exit(1)

    # relative path
    path = os.path.abspath('.') + '/' + argv[1]
    if not os.path.exists(path):
        # absolute path
        path = argv[1]
    # read file
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            splits = line.split(',')
            validate_address(line, splits[0])
            validate_amount(line, splits[1])


def main(argv=None):
    if argv is None:
        argv = sys.argv
        validate_input(argv)


if __name__ == "__main__":
    sys.exit(main())

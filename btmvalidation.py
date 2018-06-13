import os
import sys
import getopt
import httprequest


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


def get_input(argv):
    global _input_path, _account_id, _password
    try:
        opts, args = getopt.getopt(argv[1:], 'i:a:p:', ['input=', 'account=', 'password='])
        if len(opts) < 3:
            raise getopt.GetoptError('lose command option parameter')
    except getopt.GetoptError as err:
        print('Input error:' + str(err) +
              '\n' + 'Example usage:' +
              '\n' + '\t./main.py -i input.txt -a 0ETRPAV900A02 -p 123456')
        sys.exit(1)
    for opt, arg in opts:
        if opt in ('-a', '--account'):
            _account_id = arg
        if opt in ('-i', '--input'):
            _input_path = arg
        if opt in ('-p', '--password'):
            _password = arg
    return _input_path, _account_id, _password


def validate_input(argv):
    input_path, account_id, password = get_input(argv)
    # relative path
    file_path = os.path.abspath('.') + os.path.sep + input_path
    if not os.path.exists(file_path):
        # absolute path
        file_path = input_path
    # read file
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            splits = line.strip().split(',')
            validate_address(line, splits[0])
            validate_amount(line, splits[1])
    return file_path, account_id, password

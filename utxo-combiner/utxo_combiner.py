import sys, getopt
from UnspentOutputs import UnspentOutputs
from connection import Connection


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hc:a:p:m:s:",
                                   ["connection=", "account=", "password=", "max_amount=", "size="])
    except getopt.GetoptError:
        print('python test.py -c <connection> -a <account_alias> -p <password>',
              '[optional] -m <max_amount> -s <size>')
        print(
            'python test.py --connection <connection> --account <account_alias> --password <password>',
            '[optional] --max_amount <max_amount> --size <size>')
        sys.exit(2)

    # print("opts", opts)

    connection = Connection.generate()
    account_alias = ""
    password = ""
    max_amount = ""
    size = ""

    for op, value in opts:
        if op in ("-c", "--connection"):
            connection = Connection(value)
            # print(connection)
        elif op in ("-a", "--account"):
            account_alias = value
            # print(account_alias)
        elif op in ("-p", "--password"):
            password = value
            # print(password)
        elif op in ("-m", "--max_amount"):
            max_amount = int(value)
            # print(max_amount)
        elif op in ("-s", "--size"):
            size = int(value)
            # print(size)
        elif op in ("-h", "--help"):
            print('python test.py -c <connection> -a <account_alias> -p <password>',
                  '[optional] -m <max_amount> -s <size>')
            print(
                'python test.py --connection <connection> --account <account_alias> --password <password>',
                '[optional] --max_amount <max_amount> --size <size>')
            sys.exit()

    UnspentOutputs.combine_utxos(connection=connection, account_alias=account_alias,
                                 password=password, max_amount=max_amount, size=size)


if __name__ == '__main__':
    main(sys.argv[1:])

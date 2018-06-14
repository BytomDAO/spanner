import sys
import httprequest


def create_address():
    address_list = list()
    for i in range(1000):
        parameter = {'account_alias': 'alice', 'account_id': '0F0CFLG7G0A08'}
        data = httprequest.post('create-account-receiver', parameter)
        address_list.append(str(data['address']).strip() + ',100000000')

    path = '/Users/john/Desktop/btm.txt'
    with open(path, 'a', encoding='utf-8') as file:
        file.write('\n'.join(address_list) + '\n')


if __name__ == "__main__":
    sys.exit(create_address())

import requests
import sys
import json


def post(host, endpoint, parameter):
    headers = {'Content-Type': 'application/json'}
    try:
        request = requests.post(host + '/' + endpoint, headers=headers, json=parameter)
    except Exception as e:
        print(str(e) + '\n'
              + 'Connection error:Make sure bytomd or vapord run at {host} before you run this script.'.format(host=host))
        sys.exit(1)
    else:
        result = json.loads(request.text)
        if not result['status'] == 'success':
            print('Server error:' + endpoint + '\n' + result['msg'])
            sys.exit(1)
        else:
            return result['data']

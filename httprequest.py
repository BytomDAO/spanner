import requests
import sys
import json

host = 'http://localhost:9888'


def post(endpoint, parameter):
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(parameter)
    try:
        request = requests.post(host + '/' + endpoint, headers=headers, data=data)
    except Exception as e:
        print(str(e) + '\n'
              + 'Connection error:Make sure bytomd run at http://localhost:9888 before you run this script.')
        sys.exit(1)
    else:
        result = json.loads(request.text)
        if not result['status'] == 'success':
            print('Server error:' + endpoint + '\n' + result['msg'])
            sys.exit(1)
        else:
            return result['data']

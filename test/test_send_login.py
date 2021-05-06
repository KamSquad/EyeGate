import sys
import requests
import json
import hashlib

username = sys.argv[1]
password = sys.argv[2]


def run_test(inp_username, inp_password):
    test_req = {'request': 'test'}
    auth_request_login = {'request': 'login',
                          'body': {'username': inp_username}}
    check_pass_request = {'request': 'hash_pass',
                          'body': {'username': inp_username,
                                   'pass': ''}}
    tests = [test_req,
             auth_request_login,
             check_pass_request]

    response_json = None
    for test in tests:
        try:
            if test == check_pass_request:
                hashed_md5 = hashlib.md5((inp_password + response_json['body']).encode('utf-8')).hexdigest()
                check_pass_request['body']['pass'] = hashed_md5
            response = requests.get('http://127.0.0.1:5000/api/login', json=test)
            response = response.content.decode('utf-8')
            response_json = json.loads(response)
            print(test, response_json)
            # print()
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    run_test(inp_username=username,
             inp_password=password)

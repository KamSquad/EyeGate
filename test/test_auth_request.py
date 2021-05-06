import sys
import requests
import json


token = sys.argv[1]


def run_test(usr_token):
    auth_test = {'request': 'test'}
    auth_no_request_key = {'body': ''}
    auth_request_request_value_invalid = {'request': 'aaa', 'body': ''}
    auth_request_body_empty = {'request': 'auth', 'body': ''}
    auth_request_token_success = {'request': 'auth', 'body': usr_token}
    auth_request_token_invalid = {'request': 'auth', 'body': usr_token[:-1]}

    tests = [auth_test,
             auth_no_request_key,
             auth_request_body_empty,
             auth_request_request_value_invalid,
             auth_request_token_invalid,
             auth_request_token_success]

    for test_request in tests:
        try:
            response = requests.get('http://127.0.0.1:5000/api/auth', json=test_request)
            response = response.content.decode('utf-8')
            response_json = json.loads(response)
            print(test_request, response_json)
            # print()
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    run_test(usr_token=token)

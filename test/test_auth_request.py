import requests
import json
import time

server_ip, token = input().split()


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
        try:  # Test Flask: 127.0.0.1:5000
            t1 = time.time()
            response = requests.get(f'http://{server_ip}/api/auth', json=test_request)
            t2 = time.time()
            response = response.content.decode('utf-8')
            response_json = json.loads(response)
            print(f'Response time: {t2 - t1:5.4f} | {test_request} | {response_json}')
            # print()
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    run_test(usr_token=token)

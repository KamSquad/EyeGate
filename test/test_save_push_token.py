import sys
import requests

auth_token = sys.argv[1]
push_token = sys.argv[2]

save_token_test = {'request': 'test'}
save_token_no_request_key = {'body': ''}
save_token_request_request_value_invalid = {'request': 'aaa', 'body': ''}
save_token_request_body_empty = {'request': 'save_token', 'body': ''}
save_token_request_auth_invalid = {'request': 'save_token', 'body': {'auth': auth_token[:-1],
                                                                     'push': push_token,
                                                                     'univer': 'КамГУ',
                                                                     'fak': 'ФМФ',
                                                                     'state': 'active'}}
save_token_request_token_success = {'request': 'save_token', 'body': {'auth': auth_token,
                                                                      'push': push_token,
                                                                      'univer': 'КамГУ',
                                                                      'fak': 'ФМФ',
                                                                      'state': 'active'}}


tests = [save_token_test,
         save_token_no_request_key,
         save_token_request_request_value_invalid,
         save_token_request_body_empty,
         save_token_request_auth_invalid,
         save_token_request_token_success]


for test_request in tests:
    try:
        response = requests.get('http://127.0.0.1:5000/api/push', json=test_request)
        response = response.content.decode('utf-8')
        print(test_request, response)
        # print()
    except Exception as ex:
        print(ex)

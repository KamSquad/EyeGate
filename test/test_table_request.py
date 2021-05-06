import sys
import requests

token = sys.argv[1]

table_test = {'request': 'test'}
table_no_request_key = {'body': ''}
table_request_request_value_invalid = {'request': 'aaa', 'body': ''}
table_request_body_empty = {'request': 'table', 'body': ''}
table_request_token_invalid = {'request': 'table', 'body': token[:-1]}
table_request_token_success = {'request': 'table', 'body': token}


tests = [table_test,
         table_no_request_key,
         table_request_request_value_invalid,
         table_request_body_empty,
         table_request_token_invalid]

tables_request = ['КамГУ ФМФ',
                  'КамГУ ФФИМК',
                  'КамГУ СЭФ',
                  'КамГУ ППФ',
                  'КамГУ СПО']

for test_request in tests:
    try:
        response = requests.get('http://127.0.0.1:5000/api/table/a/a', json=test_request)
        response = response.content.decode('utf-8')
        print(test_request, response)
        # print()
    except Exception as ex:
        print(ex)

# success requests
for req in tables_request:
    try:
        univer, fak = req.split()
        response = requests.get(f'http://127.0.0.1:5000/api/table/{univer}/{fak}',
                                json=table_request_token_success)
        response = response.content.decode('utf-8')
        print(univer, fak, table_request_token_success, response)
        # print()
    except Exception as ex:
        print(ex)


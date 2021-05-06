import json

from lib.network import socket_api as sa

r_test = {'request': 'test'}
r_no_request_key = {'body': ''}
r_request_value_invalid = {'request': 'aaa'}
r_success = {'request': 'get_token_active_list'}


tests = [r_test,
         r_no_request_key,
         r_request_value_invalid,
         r_success]


for test_request in tests:
    try:
        request_bytes = json.dumps(test_request).encode('utf-8')
        response = sa.get_socket_answer(port=2284, content=request_bytes)
        response = response.decode('utf-8')
        print(test_request, response)
        # print()
    except Exception as ex:
        print(ex)

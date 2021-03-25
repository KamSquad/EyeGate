import sys
import requests
import json
import hashlib


username = sys.argv[1]
password = sys.argv[2]


auth_request_login = {'request': 'login',
                      'body': username}


test_req = {'request': 'test'}
response = requests.get('http://127.0.0.1:5000/api/login', json=test_req)
response = response.content.decode('utf-8')
print(response)

response = requests.get('http://127.0.0.1:5000/api/login', json=auth_request_login)
try:
    response = json.loads(response.content)
except:
    pass

print(response)

check_pass_request = {'request': 'hash_pass',
                      'body': {'username': username,
                               'pass': ''
                               }
                      }
hashed_md5 = hashlib.md5((password + response['body']).encode('utf-8')).hexdigest()
check_pass_request['body']['pass'] = hashed_md5
response = requests.get('http://127.0.0.1:5000/api/login', json=check_pass_request)
try:
    response = json.loads(response.content)
except:
    pass

print(response)
print()

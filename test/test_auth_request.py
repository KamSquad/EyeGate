import sys
import requests

token = sys.argv[1]

auth_request = {'request': 'auth',
                'body': token}

response = requests.get('http://127.0.0.1:5000/api/auth', json=auth_request)
response = response.content.decode('utf-8')
print(response)

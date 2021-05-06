import sys
import requests
import json

auth_token = sys.argv[1]
time_text_format = '%Y-%m-%d %H:%M:%S'

r_test = {'request': 'test'}
r_dyn_news_start = {'request': 'get_news', 'body': {'auth': auth_token}}
r_dyn_news_next = {'request': 'get_news', 'body': {'auth': auth_token,
                                                   'last_time': 0}}

tests = [r_test,
         r_dyn_news_start,
         r_dyn_news_next]

response = {}
for test in tests:
    try:
        # If next parts of news list. News_next request must be at the end of test list after news_start
        if tests[-1] == test:
            try:
                while True:
                    # last_news_time = datetime.strptime(response['body'][-1]['datetime'], time_text_format)
                    last_news_time = response['body'][-1]['datetime']
                    r_dyn_news_next['body']['last_time'] = last_news_time
                    response = requests.get('http://127.0.0.1:5000/api/news', json=r_dyn_news_next)
                    response = json.loads(response.content)
                    print(test, response)
                    # check end of listing
                    if 'Directed by Robert B. Weide.' in response['body']:
                        quit()

                    # print()
            except IndexError:
                quit()

        response = requests.get('http://127.0.0.1:5000/api/news', json=test)
        response = json.loads(response.content)
        print(test, response)
        # print()
    except Exception as ex:
        print(ex)

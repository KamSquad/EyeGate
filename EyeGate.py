from flask import Flask, request

import json
import bjoern
from lib.network import socket_api as sa
from lib import thread

app = Flask(__name__)


@app.route('/status')
def gate_status():
    return 'Status: online'


@app.route('/api/auth', methods=['GET', 'POST'])
def auth_request():
    """
    Thread login router
    :return: auth result
    """
    # print('api/auth')
    content = request.json
    auth_answer = thread.run(thread_function=auth_request_thread,
                             args=content)
    return auth_answer


def auth_request_thread(content, queue_res):
    """
    Connect login microservice and get result in every thread
    :param content:
    :param queue_res:
    :return:
    """
    content = json.dumps(content).encode('utf-8')
    sa.get_socket_answer(port=2289, content=content, queue_object=queue_res)


@app.route('/api/login', methods=['GET', 'POST'])
def login_request():
    """
    Thread login router
    :return: auth result
    """
    # print('api/login')
    content = request.json
    auth_answer = thread.run(thread_function=login_request_thread,
                             args=content)
    return auth_answer


def login_request_thread(content, queue_res):
    """
    Connect login microservice and get result in every thread
    :param content:
    :param queue_res:
    :return:
    """
    content = json.dumps(content).encode('utf-8')
    sa.get_socket_answer(port=2288, content=content, queue_object=queue_res)


@app.route('/api/push', methods=['GET', 'POST'])
def push_request():
    """
    Thread push server router
    :return: push server result
    """
    # print('api/push')
    content = request.json
    auth_answer = thread.run(thread_function=push_request_thread,
                             args=content)
    return auth_answer


def push_request_thread(content, queue_res):
    """
    Connect login microservice and get result in every thread
    :param content:
    :param queue_res:
    :return:
    """
    content = json.dumps(content).encode('utf-8')
    sa.get_socket_answer(port=2283, content=content, queue_object=queue_res)


@app.route('/api/news', methods=['GET', 'POST'])
def news_request():
    """
    Thread push server router
    :return: push server result
    """
    # print('api/push')
    content = request.json
    auth_answer = thread.run(thread_function=news_request_thread,
                             args=content)
    return auth_answer


def news_request_thread(content, queue_res):
    """
    Connect login microservice and get result in every thread
    :param content:
    :param queue_res:
    :return:
    """
    content = json.dumps(content).encode('utf-8')
    sa.get_socket_answer(port=2290, content=content, queue_object=queue_res, long_answer=True)


# 1. ip:5000/register with json
# 2. ip:5000/'<client-id>'/


# @app.route('/api/timetable/<string:univer>/<string:fak>')
# def get_covid_states_report_by_country(univer, fak):
#    return fak


def main():
    bjoern.run(app, "127.0.0.1", 5000)
    # app.run()


if __name__ == '__main__':
    main()

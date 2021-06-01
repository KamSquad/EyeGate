from flask import Flask, request

import json
import bjoern
from lib.network import socket_api as sa
from lib import thread
from lib import config

app = Flask(__name__)
c = config.EnvConfig()


@app.route(c.routes.status)
def gate_status():
    return 'Status: online'


@app.route(c.routes.auth, methods=['GET', 'POST'])
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
    sa.get_socket_answer(port=c.m_ports.auth, content=content, queue_object=queue_res)


@app.route(c.routes.login, methods=['GET', 'POST'])
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
    sa.get_socket_answer(port=c.m_ports.login, content=content, queue_object=queue_res)


@app.route(c.routes.push, methods=['GET', 'POST'])
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
    sa.get_socket_answer(port=c.m_ports.push, content=content, queue_object=queue_res)


@app.route(c.routes.news, methods=['GET', 'POST'])
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
    sa.get_socket_answer(port=c.m_ports.news, content=content, queue_object=queue_res, long_answer=True)


# 1. ip:5000/register with json
# 2. ip:5000/'<client-id>'/M_PORT_AUTH", default=2289


# @app.route('/api/timetable/<string:univer>/<string:fak>')
# def get_covid_states_report_by_country(univer, fak):
#    return fak


def main():
    c.print_params()
    print(f'Server started on {c.gate.allowed_hosts}:{c.gate.port}.. ')
    bjoern.run(app, c.gate.allowed_hosts, c.gate.port)


if __name__ == '__main__':
    main()

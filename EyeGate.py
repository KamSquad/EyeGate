from flask import Flask, request

import json
import bjoern
from lib.network import socket_api as sa
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
    auth_answer = None
    content = request.json
    content = json.dumps(content).encode('utf-8')
    try:
        auth_answer = sa.get_socket_answer(port=c.m_ports.auth, content=content)
    except:
        pass
    return auth_answer


@app.route(c.routes.login, methods=['GET', 'POST'])
def login_request():
    """
    Thread login router
    :return: auth result
    """
    # print('api/login')
    auth_answer = None
    content = request.json
    content = json.dumps(content).encode('utf-8')
    try:
        auth_answer = sa.get_socket_answer(port=c.m_ports.login, content=content)
    except:
        pass
    return auth_answer


@app.route(c.routes.push, methods=['GET', 'POST'])
def push_request():
    """
    Thread push server router
    :return: push server result
    """
    # print('api/push')
    auth_answer = None
    content = request.json
    content = json.dumps(content).encode('utf-8')
    try:
        auth_answer = sa.get_socket_answer(port=c.m_ports.push, content=content)
    except:
        pass
    return auth_answer


@app.route(c.routes.news, methods=['GET', 'POST'])
def news_request():
    """
    Thread push server router
    :return: push server result
    """
    # print('api/push')
    auth_answer = None
    content = request.json
    content = json.dumps(content).encode('utf-8')
    try:
        auth_answer = sa.get_socket_answer(port=c.m_ports.news, content=content, long_answer=True)
    except:
        pass
    return auth_answer


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

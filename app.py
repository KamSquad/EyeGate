from flask import Flask, request, jsonify
from threading import Thread

import socket
import json
import queue


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
    content = request.json
    queued_request = queue.Queue()
    Thread(target=auth_thread_request, args=(content, queued_request)).start()
    auth_answer = queued_request.get()
    return auth_answer


def auth_thread_request(content, queue_res):
    """
    Connect login microservice and get result in every thread
    :param content:
    :param queue_res:
    :return:
    """
    content = json.dumps(content).encode('utf-8')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 2289))
    client.send(content)
    resp = client.recv(1024)
    if resp:
        queue_res.put(resp)
    else:  # TODO: fill else if empty/None answer
        print('empty')


@app.route('/api/login', methods=['GET', 'POST'])
def login_request():
    """
    Thread login router
    :return: auth result
    """
    content = request.json
    queued_request = queue.Queue()
    Thread(target=login_thread_request, args=(content, queued_request)).start()
    auth_answer = queued_request.get()
    return auth_answer


def login_thread_request(content, queue_res):
    """
    Connect login microservice and get result in every thread
    :param content:
    :param queue_res:
    :return:
    """
    content = json.dumps(content).encode('utf-8')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 2288))
    client.send(content)
    resp = client.recv(1024)
    if resp:
        queue_res.put(resp)
    else:  # TODO: fill else if empty/None answer
        print('empty')


# 1. ip:5000/register with json
# 2. ip:5000/'<client-id>'/


# @app.route('/api/timetable/<string:univer>/<string:fak>')
# def get_covid_states_report_by_country(univer, fak):
#    return fak


if __name__ == '__main__':
    app.run()

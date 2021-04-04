import json
import socket
import time

from lib.network import net_request as nr


class Socket:
    def __init__(self, port):
        self.sock = None
        self.port = port
        self.conn = None
        self.addr = None
        self.create()

    def create(self):
        try:
            self.sock = socket.socket()
            self.sock.bind(('', self.port))
        except Exception as ex:
            print(ex, ', waiting 10 secs..')
            time.sleep(10)
            self.create()

    def listen(self):
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()

    def connect(self, port, host='localhost'):
        self.sock.connect((host, port))

    def get_data(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            return json.loads(data)

    def get_answer(self, data):
        data = json.dumps(data).encode('utf-8')
        self.sock.send(data)
        ans = self.sock.recv(1024).decode('utf-8')
        if ans != '':
            ans = json.loads(ans)
        return ans

    def send_data_after_listen(self, data):
        data = json.dumps(data).encode('utf-8')
        self.conn.send(data)
        # self.close()

    def close(self):
        self.conn.close()


def get_socket_answer(port, content, queue_object, ip='127.0.0.1'):
    """
    Get answer from microservice by socket
    :type port: int
    :param port: microservice port
    :type ip: str
    :param ip: microservice ip address
    :type content: bytes
    :param content: content to send
    :type queue.Queue() object
    :param queue_object: queue object to put answer
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    client.send(content)
    resp = client.recv(1024)
    if resp:
        queue_object.put(resp)
    else:  # TODO: fill else if empty/None answer
        err_answer = nr.make_answer_json(answer_code=nr.answer_codes['failed'],
                                         body='auth failed')
        err_answer = json.dumps(err_answer).encode('utf-8')
        queue_object.put(err_answer)

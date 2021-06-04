import json
import socket
import struct
import time
from lib.network import net_request as nr


block_size = 1024  # block size to send/receive socket messages


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
            data = self.conn.recv(block_size)
            if not data:
                break
            return json.loads(data)

    def get_answer(self, data):
        data = json.dumps(data).encode('utf-8')
        self.sock.send(data)
        ans = self.sock.recv(block_size).decode('utf-8')
        if ans != '':
            ans = json.loads(ans)
        return ans

    def send_data_after_listen(self, data):
        data = json.dumps(data).encode('utf-8')
        self.conn.send(data)
        # self.close()

    def close(self):
        self.conn.close()


def get_socket_answer(port, content, ip='127.0.0.1', queue_object=None, long_answer=False):
    """
    Get answer from microservice by socket
    :param long_answer: use stream answer receive
    :type port: int
    :param port: microservice port
    :type ip: str
    :param ip: microservice ip address
    :type content: bytes
    :param content: content to send
    :type queue_object Queue() object
    :param queue_object: queue object to put answer
    """
    resp = None
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(ip, port)
        client.connect((ip, port))
        # send request
        client.send(content)
        # get socket answer
        if not long_answer:
            resp = client.recv(block_size)
        else:
            resp = recv_msg(client)
    # exception on socket connect error
    except Exception as ex:
        print(ex)
    # set fail answer
    if not resp:
        resp = nr.make_answer_json(answer_code=nr.answer_codes['failed'],
                                   body='empty answer')
        resp = json.dumps(resp).encode('utf-8')

    if queue_object:
        queue_object.put(resp)
    else:
        return resp


def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msg_len = recv_all(sock, 4)
    if not raw_msg_len:
        return None
    msg_len = struct.unpack('>I', raw_msg_len)[0]
    # Read the message data
    return recv_all(sock, msg_len)


def recv_all(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data

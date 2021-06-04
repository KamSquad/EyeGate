import os
from collections import namedtuple
from dotenv import load_dotenv
from pprint import pprint


class EnvConfig:
    def __init__(self):
        """
        Get environment variables
        """
        try:
            load_dotenv('.env')
        except:
            load_dotenv('../.env')
        self.gate = namedtuple('gate', 'allowed_hosts port m_services_host')
        self.gate.allowed_hosts = str(os.environ.get("GATE_ALLOWED_HOSTS", default="127.0.0.1"))
        self.gate.port = int(os.environ.get("GATE_PORT", default=5000))
        self.gate.m_services_host = str(os.environ.get("GATE_M_SERVICES_HOST", default="127.0.0.1"))

        self.routes = namedtuple('routes', 'status auth news login push')
        self.routes.status = str(os.environ.get("ROUTES_STATUS", default="/status"))
        self.routes.auth = str(os.environ.get("ROUTES_AUTH", default="/api/auth"))
        self.routes.login = str(os.environ.get("ROUTES_LOGIN", default="/api/login"))
        self.routes.push = str(os.environ.get("ROUTES_PUSH", default="/api/push"))
        self.routes.news = str(os.environ.get("ROUTES_NEWS", default="/api/news"))

        self.m_ports = namedtuple('m_ports', 'auth news login push')
        self.m_ports.auth = int(os.environ.get("M_PORT_AUTH", default=2289))
        self.m_ports.login = int(os.environ.get("M_PORT_LOGIN", default=2288))
        self.m_ports.push = int(os.environ.get("M_PORT_PUSH", default=2283))
        self.m_ports.news = int(os.environ.get("M_PORT_NEWS", default=2290))

    def print_params(self):
        params = [self.gate, self.routes, self.m_ports]
        for param in params:
            new_param = {}
            param_dict = dict(vars(param))
            for value in param_dict:
                # print()
                if not value.startswith('_'):
                    new_param[value] = param_dict[value]
            pprint(new_param)

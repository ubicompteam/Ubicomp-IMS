import http.client

from panopticon.base_observer.observing import BaseObserver
from panopticon.base_observer.response import ObserverResponse

class WebObserver(BaseObserver):
    def __init__(self, hostname: str, port: int, headers=None, timeout: int = 5):
        if headers is None:
            headers = dict()
        self.hostname = hostname
        self.port = port
        self.headers = headers
        self.timeout = timeout

    def check(self):
        try:
            conn = http.client.HTTPConnection(self.hostname, self.port, timeout=self.timeout)
            conn.request("GET", "/", headers=self.headers)
            response = conn.getresponse()
            ret = ObserverResponse(status=True, data=response.status)
        except Exception as e:
            ret = ObserverResponse(status=False, message=str(e))
        return ret
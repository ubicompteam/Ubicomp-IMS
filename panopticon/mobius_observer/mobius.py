import http.client
import datetime
import json

from panopticon.base_observer.observing import BaseObserver
from panopticon.base_observer.response import ObserverResponse


class Mobius:
    def __init__(self, hostname: str, port: int, headers: dict):
        self.hostname = hostname
        self.port = port
        self.headers = headers

    def get_observer(self, observer_type, **kwargs):
        if observer_type == "ping":
            return PingObserver(self.hostname, self.port, self.headers, **kwargs)
        elif observer_type == "interval":
            return IntervalObserver(self.hostname, self.port, self.headers, **kwargs)
        else:
            raise ValueError("Invalid observer type")

class PingObserver(BaseObserver):
    def __init__(self, hostname: str, port: int, headers: dict, timeout: int = 5):
        self.hostname = hostname
        self.port = port
        self.headers = headers
        self.timeout = timeout
    def check(self):
        try:
            conn = http.client.HTTPConnection(self.hostname, self.port, timeout=self.timeout)
            conn.request("GET", "/", headers=self.headers)
            response = conn.getresponse()
            ret = ObserverResponse(status=True, data=response.read())
        except Exception as e:
            ret = ObserverResponse(status=False, message=str(e))
        return ret

class IntervalObserver(BaseObserver):
    def __init__(self, hostname: str, port: int, headers: dict, resource: str, interval: int | datetime.timedelta):
        self.hostname = hostname
        self.port = port
        self.headers = headers
        self.timeout = 5
        self.interval = interval
        self.resource = resource + '/la'

        if isinstance(interval, int):
            self.interval = datetime.timedelta(minutes=interval)

        if self.interval.total_seconds() < 1:
            raise ValueError("Interval must be at least 1 second")
    def check(self):
        try:
            conn = http.client.HTTPConnection(self.hostname, self.port, timeout=self.timeout)
            conn.request("GET", self.resource, headers=self.headers)
            response = conn.getresponse()
            ret = json.loads(response.read())
            ret = ret['m2m:cin']['con'].split(',')[0]
            ret = datetime.datetime.strptime(ret, '%Y%m%d%H%M%S')
            ret = ObserverResponse(status=datetime.datetime.now() - ret < self.interval, data=ret)
        except Exception as e:
            ret = ObserverResponse(status=False, message=str(e))
        return ret
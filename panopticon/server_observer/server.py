from base_observer.observing import BaseObserver
from base_observer.response import ObserverResponse
from utils.ping import Ping

class ServerObserver(BaseObserver):
    def __init__(self, ip: str, timeout: int = 1):
        self.ip = ip
        self.timeout = timeout

    def check(self):
        try:
            ping = Ping(self.ip, self.timeout)
            ret = ping.send_echo_request()

            if ret:
                ret = ObserverResponse(status=True, data=ret)
            else:
                ret = ObserverResponse(status=False, message="No response")
        except Exception as e:
            ret = ObserverResponse(status=False, message=str(e))
        return ret
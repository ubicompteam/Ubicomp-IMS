import datetime
import socket
import time


def _log(message):
    print(message)
    with open("log.txt", "a") as f:
        f.write(message + "\n")

class Client:
    def __init__(self, host, port):
        self.interval = None
        self.observer = None
        self.host = host
        self.port = port
        
        # self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.connect()
        # for i in range(10):
        while True:
            try:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.connect()
                break
            except Exception as e:
                _log(f"[{datetime.datetime.now()}] Error: {str(e)}")
                time.sleep(10)

        # if i == 9:
        #     raise Exception("Failed to connect to the server")

    def set_observer(self, observer, interval = 10):
        self.observer = observer
        self.interval = interval

    def check(self):
        return self.observer.check()

    def start(self, retry_forever = False):
        while True:
            try:
                data = self.check()
                self.client.sendall(str(data).encode())
                _log(f"[{datetime.datetime.now()}] Sent: {data}")
            except Exception as e:
                _log(f"[{datetime.datetime.now()}] Error: {str(e)}")
                if not retry_forever:
                    self.client.close()
                    return
                # self.client.close()
                self.connect()
            time.sleep(self.interval)
        # self.client.close()

    def connect(self, retry_forever = True):
        while True:
            try:
                self.client.connect((self.host, self.port))
                print("Connected to the server")
                _log(f"[{datetime.datetime.now()}] Connected to {self.host}:{self.port}")
                break
            except Exception as e:
                _log(f"[{datetime.datetime.now()}] Error: {str(e)}")
                if not retry_forever:
                    break
                time.sleep(self.interval)

    def __del__(self):
        self.client.close()
        print("Client stopped")
        _log(f"[{datetime.datetime.now()}] Connection closed")


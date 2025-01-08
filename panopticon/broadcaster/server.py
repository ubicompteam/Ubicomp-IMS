import socket
import time
import datetime
from _thread import *


def _log(message):
    print(message)
    with open("log.txt", "a") as f:
        f.write(message + "\n")


class Server:
    def __init__(self, host = socket.gethostbyname(socket.gethostname()), port = 5555):
        self.interval = None
        self.observer = None
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def set_observer(self, observer, interval = 10):
        self.observer = observer
        self.interval = interval

    def _send(self, conn, data):
        try:
            conn.sendall(data.encode())
            _log(f"[{datetime.datetime.now()}] Sent: {data}")
        except Exception as e:
            _log(f"[{datetime.datetime.now()}] Error: {str(e)}")

    def _handle_client(self, conn):
        while True:
            try:
                data = self.observer.check()
                self._send(conn, str(data))
                time.sleep(self.interval)
            except Exception as e:
                _log(f"[{datetime.datetime.now()}] Error: {str(e)}")
                break
        conn.close()
        _log(f"[{datetime.datetime.now()}] Connection closed")

    def start(self):
        try:
            self.server.bind((self.host, self.port))
        except socket.error as e:
            _log(str(e))
        self.server.listen(5)
        while True:
            conn, addr = self.server.accept()
            _log(f"[{datetime.datetime.now()}] Connected to {addr[0]}:{addr[1]}")
            start_new_thread(self._handle_client, (conn,))
        self.server.close()
        _log("Server stopped")

    def __del__(self):
        self.server.close()
        _log("Server stopped")


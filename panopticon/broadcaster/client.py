import socket
import time

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def connect(self):
        while True:
            data = self.client.recv(1024)
            while not data:
                data = self.client.recv(1024)
            print(data.decode())
            time.sleep(1)

    def __del__(self):
        self.client.close()
        print("Client stopped")


if __name__ == "__main__":
    client = Client("localhost", 5555)
    client.connect()
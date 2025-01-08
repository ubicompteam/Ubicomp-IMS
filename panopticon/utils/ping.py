import socket
import struct

class Ping:
    def __init__(self, ip, timeout = 1):
        self.ip = ip
        self.timeout = timeout

    def send_echo_request(self):
        with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as s:
            packet = self.create_packet()
            s.sendto(packet, (self.ip, 1))

            s.settimeout(self.timeout)
            try:
                data, _ = s.recvfrom(1024)
                return data
            except socket.timeout:
                return None

    def create_packet(self):
        checksum = 0
        header = struct.pack("!BBHHH", 8, 0, checksum, 0, 0)
        data = b"Hello, World!"
        checksum = self.checksum(header + data)
        header = struct.pack("!BBHHH", 8, 0, checksum, 0, 0)
        return header + data

    def checksum(self, data):
        if len(data) % 2:
            data += b"\x00"
        s = sum(struct.unpack("!H", data[i:i+2])[0] for i in range(0, len(data), 2))
        s = (s >> 16) + (s & 0xffff)
        s += s >> 16
        return ~s & 0xffff
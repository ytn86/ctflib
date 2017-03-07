
import telnetlib
import struct


class Pwn(object):

    def __init__(self):
        self.tn = None
        self.sock = None

        
    def connect(self, host: str, port: int):
        self.tn = telnetlib.Telnet(host, port)
        self.sock = self.tn.get_socket()


    def read_until(self, delim: bytes):
        data = b''
        while not data.endswith(delim):
            data += self.sock.recv(1)
        return data


    def recv(self, size: int):
        return self.sock.recv(size)


    def send(self, data: bytes):
        self.sock.send(data)


    def interact(self):
        self.tn.interact()
    

import struct


def pI(addr: int):
    return struct.pack('<I', addr)


def upI(addr: bytes):
    return struct.unpack('<I', addr)[0]


def pQ(addr: int):
    return struct.pack('<Q', addr)    
    

def upQ(addr: bytes):
    return struct.unpack('<Q', addr)[0]


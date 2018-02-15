import socket


s = socket.socket()
s.connect(("localhost", 9999))
f = open("IMG_20160125_0642271.jpg", "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
s.close()

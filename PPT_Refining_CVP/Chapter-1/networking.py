import socket

socket.setdefaulttimeout(2)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("64.13.134.52", 80))
data = s.recv(1024)
print(data.decode())
s.close()

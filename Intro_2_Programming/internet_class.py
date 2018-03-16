
import socket

IP = ' 172.17.29.154'
REMOTEIP = '172.17.18.216'
port = 8080

# Use a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# internet can be summed up in TCP/IP
# UDP - unreliable

# connect to the other computer!
s.connect((REMOTEIP, port))

s.sendall(b'HELLO WORLD')

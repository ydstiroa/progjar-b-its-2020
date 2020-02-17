import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

f = open("dikirim.txt", "rb")
l = f.read(1024)
while (l):
    sock.send(l)
    l = f.read(1024)
sock.close()
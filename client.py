import socket
import sys
import time
s = socket.socket()
host = input(str("please enter host name"))
port = 1234
try:
    s.connect((host,port))
    print("connected to the server")
except:
    print("connection to server is failed")
while 1:
    incoming_msg = s.recv(1024)
    incoming_msg = incoming_msg.decode()
    print("Server:>>",incoming_msg)
    message = input(str("You:>>"))
    message = message.encode()
    s.send(message)
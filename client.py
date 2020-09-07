import socket
import subprocess

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5003
BUFFER_SIZE = 1024
# create the socket object
s = socket.socket()
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
# receive the greeting message
message = s.recv(BUFFER_SIZE).decode()
print("Server:", message)
while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    print(command)
    output = input("enter your message: ")
    # send the message to server
    s.send(output.encode())
#close connection
s.close()
import socket
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5003
# send 1024 (1kb) a time (as buffer size)
BUFFER_SIZE = 1024
# create a socket object
s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
get_host = socket.gethostname()
print(get_host)
print(f"Waiting for connection ...")
# accept any connections attempted
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")
get_host = socket.gethostname()
print(get_host)
message = "Hello and Welcome".encode()
client_socket.send(message)
while True:
    # get the command from prompt
    command = input("Enter the message you wanna send: ")
    # send the command to the client
    client_socket.send(command.encode())
    
    results = client_socket.recv(BUFFER_SIZE).decode()
    # print them
    print(results)
# close connection to the client
client_socket.close()
# close server connection
s.close()
import socket

server_addr = ('0.0.0.0', 6666)

# create a TCP socket & listen on server_addr
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(server_addr)
tcp_socket.listen(1)
print('Ready to receive TCP pakcets')

while True:
    # accept the connection request from the client
    connection_socket, client_addr = tcp_socket.accept()

    # receive a message from the client
    msg = connection_socket.recv(1024)
    print(f"Received message: '{msg.decode()}' from {client_addr}")

    # send a new message back to the client
    new_msg = msg.decode().upper()
    connection_socket.send(new_msg.encode())
    print(f"Sent new message: '{new_msg}' back to {client_addr}")

    # close the connection
    connection_socket.close()
# end while

tcp_socket.close()
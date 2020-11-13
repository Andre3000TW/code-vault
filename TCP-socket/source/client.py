import socket

server_addr = ('server_ip', 6666)

# create a TCP socket & connect to the server
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(server_addr)

# send a message to the server
msg = 'msg'
tcp_socket.send(msg.encode())
print(f"Message: '{msg}' has been sent")

# receive a new message from the server
new_msg = tcp_socket.recv(1024)
print(f"New message: '{new_msg.decode()}' has received")

# close the connection
tcp_socket.close()
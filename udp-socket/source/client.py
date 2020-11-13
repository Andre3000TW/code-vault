import socket

server_addr = ('server_ip', 6666)

# create an UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send a message to the server
msg = 'msg'
udp_socket.sendto(msg.encode(), server_addr)
print(f"Message: '{msg}' has been sent")

# receive a new message from the server
new_msg, return_addr = udp_socket.recvfrom(1024)
print(f"New message: '{new_msg.decode()}' has received [from {return_addr}]")

udp_socket.close()

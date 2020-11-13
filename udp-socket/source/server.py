import socket

# create an UDP socket
server_addr = ('0.0.0.0', 6666)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(server_addr)
print('Ready to receive UDP packets')

while True:
    # receive a message from the client
    msg, client_addr = udp_socket.recvfrom(1024)
    print(f"Received message: '{msg.decode()}' from {client_addr}")

    # send a new message back to the client
    new_msg = msg.decode().upper()
    udp_socket.sendto(new_msg.encode(), client_addr)
    print(f"Sent new message: '{new_msg}' back to {client_addr}")
# end while

udp_socket.close()

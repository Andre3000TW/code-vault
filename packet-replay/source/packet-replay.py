import time
import binascii
from struct import pack
from socket import socket, AF_PACKET, SOCK_RAW

try:
    interval = float(input('Enter time interval(s): '))
    print(interval)

    # create a raw socket
    raw_socket = socket(AF_PACKET, SOCK_RAW)
    raw_socket.bind(('interface_name', 0))

    # prepare the packet to be replayed
    byte_list = []
    hex_stream = 'hex_stream_to_be_replayed'
    num_of_bytes = str(len(hex_stream) // 2)
    for index in range(0, len(hex_stream), 2): byte_list.append(int('0x' + hex_stream[index:index+2], 16))
    packet = pack('!' + num_of_bytes + 'B', *byte_list)

    # send out the packet at every interval
    while True:
        raw_socket.send(packet)
        print('Pakcet replayed')
        time.sleep(interval)
    # end while
except KeyboardInterrupt:
    print('Keyboard Interrupted')
    raw_socket.close()
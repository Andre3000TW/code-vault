import binascii
from struct import pack, unpack
from socket import socket, AF_PACKET, SOCK_RAW, htons

# create a raw socket
s = socket(AF_PACKET, SOCK_RAW, htons(0x0806)) # ARP type number(0x0800 for IP, 0x0003 for all ethernet frame)
s.bind(('eth0', 0))

# pack the frame & send it out
# ! => big-endian
# B => unsigned char  (1 bytes)
# H => unsigned short (2 bytes)
frame = [
    # ethernet
    pack('!6B', *[0xff, 0xff, 0xff, 0xff, 0xff, 0xff]), # Destination
    pack('!6B', *[0x08, 0x00, 0x27, 0x1f, 0x30, 0x76]), # Source
    pack('!H', 0x0806), # Type: ARP(0x0806)
    # arp
    pack('!H', 0x0001), # Hardware type: Ethernet
    pack('!H', 0x0800), # Protocol type: IPv4
    pack('!B', 0x06),   # Hardware size: 6
    pack('!B', 0x04),   # Protocol size: 4
    pack('!H', 0x0001), # Opcode: request(1)
    pack('!6B', *[0x08, 0x00, 0x27, 0x1f, 0x30, 0x76]), # Sender MAC address
    pack('!4B', *[192, 168, 1, 4]), # Sender IP address
    pack('!6B', *[0x00, 0x00, 0x00, 0x00, 0x00, 0x00]), # Target MAC address
    pack('!4B', *[192, 168, 1, 20])  # Target IP address
]
s.send(b''.join(frame))

# receive the frame & unpack it
# s => char[]
frame = s.recvfrom(2048)
ethernet_frame = unpack("!6s6s2s", frame[0][0:14]) # extract ethernet frame
arp_frame = unpack("2s2s1s1s2s6s4s6s4s", frame[0][14:42]) # extract arp frame

# extract target host MAC address in the arp frame
target_mac = binascii.hexlify(arp_frame[5]).decode().upper()
target_mac = ':'.join(target_mac[x:y] for x, y in zip(range(0, 10 + 1, 2), range(2, 12 + 1, 2)))
print(f'Target Host MAC address: {target_mac}')

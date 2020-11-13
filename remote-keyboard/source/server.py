import socket
import requests
from bs4 import BeautifulSoup

import keyboard
from datetime import datetime

# get ip addr
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
page = requests.get('https://whatismyipaddress.com', headers=headers)
page.encoding = 'utf8'
soup = BeautifulSoup(page.text, 'lxml')
ip_addr = soup.find('a', text='Show Complete IP Details').get('href').split('/')[-1]

# create an UDP socket
server_addr = ('0.0.0.0', 6666)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(server_addr)
print(f'Ready to receive commands on port: {server_addr[1]} with public IP addr: {ip_addr}')

while True:
    key, client_addr = udp_socket.recvfrom(1024)
    key = key.decode()
    print(f'Received key: {key} at {datetime.now().strftime("%Y/%m/%d %I:%M:%S%p")} from {client_addr}')

    keyboard.send(key)
# end while

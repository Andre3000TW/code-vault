import time
import socket
import keyboard

def keydownEventHanlder(key):
    udp_socket.sendto(key.name.encode(), server_addr)
    print(f"Key: '{key.name}' sent")
# end keydownEventHanlder()

try:
    server_addr = ('server_ip', 6666)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    keys = ['esc', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', '`',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '=', 'backspace', 'tab',
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', 'caps lock',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'enter', 'shift',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.',
            'right shift', 'ctrl', 'left windows', 'alt', 'space', 'right alt', 'menu', 'right ctrl',
            'print screen', 'scroll lock', 'pause', 'insert', 'home', 'page up', 'delete', 'end', 'page down',
            'up', 'left', 'down', 'right', 'decimal', '+', '-', '*', '/', 'num lock'
    ]

    for key in keys: keyboard.on_press_key(key, keydownEventHanlder)

    print(f'Ready to send keydown events to {server_addr}')
    while True: time.sleep(1)
except KeyboardInterrupt:
    print('ERROR: Interrupted by user')
finally:
    udp_socket.close()
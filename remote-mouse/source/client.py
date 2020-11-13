import time
import socket
import mouse

def mouseEventHandler(event):
    msg = ''
    if type(event).__name__ == 'MoveEvent': msg = f'move:{event.x},{event.y}'
    elif type(event).__name__ == 'WheelEvent': msg = f'wheel:{event.delta}'
    elif type(event).__name__ == 'ButtonEvent': msg = f'button {event.event_type}:{event.button}'
    else: msg = 'error:unknown event'

    udp_socket.sendto(msg.encode(), server_addr)
    print(f'Message: {msg} sent')
# end mouseEventHandler()

try:
    server_addr = ('server_ip', 6666)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    mouse.hook(mouseEventHandler)

    print(f'Ready to send mouse events to {server_addr}')
    while True: time.sleep(1)
except KeyboardInterrupt:
    print('ERROR: Interrupted by user')
finally:
    udp_socket.close()
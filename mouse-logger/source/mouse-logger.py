import time
import mouse

def logger(event):
    with open('mouselog.txt', 'a') as mouselog:
        msg = ''
        if type(event).__name__ == 'MoveEvent': msg = f'move:{event.x},{event.y}'
        elif type(event).__name__ == 'WheelEvent': msg = f'wheel:{event.delta}'
        elif type(event).__name__ == 'ButtonEvent': msg = f'button {event.event_type}:{event.button}'
        else: msg = 'error:unknown event'
            
        mouselog.write(msg + '\n')
        print(msg)
    # end with-as
# end logger()

mouse.hook(logger)

while True: time.sleep(1)

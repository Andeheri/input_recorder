from pynput.mouse import Listener, Controller
import pynput
import keyboard
import logging  
import win32api

mouse = Controller()

mouse_log_file = 'select_capsules_120.txt'

logging.basicConfig(filename=mouse_log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_move(x, y):
    x, y = mouse.position 
    logging.info(f'MOVE {x},{y}')

def on_click(x, y, button, pressed):
    if not pressed:
        logging.info(f'CLICK {button}')

def on_scroll(x, y, dx, dy):
    logging.info(f'SCROLL {dx},{dy}')

def on_press(key):
    if key == pynput.keyboard.Key.space:
        # Stop listener 
        return False  

def main():
    print('Press \'space\' to start and stop.')
    pressed = False 
    while True:
        if keyboard.is_pressed('space'):
            pressed = True 
        elif not keyboard.is_pressed('space') and pressed:
            break
    print('Started')
    # Clears file
    with open(mouse_log_file, 'w') as f:
        pass
    win32api.Beep(700, 200)
    # Start keyboard listener
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()
    # Start mouse listener
    with Listener(on_scroll=on_scroll, on_click=on_click, on_move=on_move) as mouse_listener:
        # Wait for enter key to be pressed
        listener.join()
        print('Stopped')
        win32api.Beep(700, 200)
        # Stop mouse listener
        mouse_listener.stop()
        mouse_listener.join()

 
if __name__ == '__main__': 
    main()
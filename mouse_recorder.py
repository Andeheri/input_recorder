from pynput.mouse import Listener, Controller
import pynput
import keyboard
import logging  
import win32api
from time import sleep

mouse = Controller()

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

def record(file: str):
    # Clears file
    with open(file, 'w') as f:
        pass
    logging.basicConfig(filename=file, level=logging.DEBUG, format='%(asctime)s: %(message)s')
    win32api.Beep(550, 1000)
    sleep(0.5)
    win32api.Beep(550, 800)
    sleep(0.5)
    win32api.Beep(800, 1300)
    # Start keyboard listener
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()
    # Start mouse listener
    with Listener(on_scroll=on_scroll, on_click=on_click, on_move=on_move) as mouse_listener:
        # Wait for enter key to be pressed
        listener.join()
        print('Stopped')
        win32api.Beep(700, 500)
        # Stop mouse listener
        mouse_listener.stop()
        mouse_listener.join()
    return True


from pynput.mouse import Controller, Button
import pynput
import keyboard
from datetime import datetime
from time import sleep
import win32api
from metal_pipe import play_mp3


mouse = Controller()
 
mouse_controller_file = 'mouse_movements/buy_capsules.txt'

num_times = 7


class Action:
    def __init__(self, action_str: str) -> None:
        self.timestamp = datetime.strptime(action_str[:23],  '%Y-%m-%d %H:%M:%S,%f')
        self.action, self.data = action_str[25:].split(' ')

    @staticmethod
    def difference_timestamps_in_sec(timestamp_1, timestamp_2):
        return abs((timestamp_1 - timestamp_2).total_seconds())
    
    def do_action(self):
        if self.action == 'MOVE':
            x, y = list(map(int, self.data.split(',')))
            mouse.position = (x, y)
        elif self.action == 'CLICK':
            print(self.data)
            if self.data == 'Button.left\n': 
                mouse.click(Button.left)
            elif self.data == 'Button.right\n':
                mouse.click(Button.right)
        elif self.action == 'SCROLL':
            dx, dy = list(map(int, self.data.split(',')))
            mouse.scroll(dx, dy)

def on_press(key):
    if key == pynput.keyboard.Key.space:
        # Stop listener 
        return False  

def main():
    with open(mouse_controller_file, 'r') as f:
        actions = f.readlines()
    
    actions = [Action(action_str) for action_str in actions]
    
    last_timestamp = actions[0].timestamp
    print('Press \'space\' to start and stop.')
    pressed = False
    while True:
        if keyboard.is_pressed('space'):
            pressed = True
        elif not keyboard.is_pressed('space') and pressed:
            break
    print('Starting')
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()
    for _ in range(num_times):
        play_mp3()
        last_timestamp = actions[0].timestamp
        actions[0].do_action()
        for i, action in enumerate(actions):
            sleep(Action.difference_timestamps_in_sec(last_timestamp, action.timestamp))
            action.do_action() 
            last_timestamp = action.timestamp


if __name__ == '__main__':
    main()
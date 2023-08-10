import keyboard
from time import sleep
import sys

def on_key_press(event):
    if event.name == 'space':
        print("Exiting the program...")
        sys.exit()

def main(): 
    while True:
        print(1)
        # Move cursor
        sleep(1)   


# Set up the keyboard event handler
keyboard.on_press(on_key_press)

# Call the main function
main()

# Keep the program running until the space key is hit
keyboard.wait('space')
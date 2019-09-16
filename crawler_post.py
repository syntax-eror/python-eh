#!/usr/bin/env python

import requests

target_url = raw_input("Enter target URL: ")
data_dict = {"username": "testui", "password": "testpw", "Login": "submit"} #field names taken from DVWA;
#<form action="login.php" method="post">
#<input class="loginInput" name="username" type="text">
response = requests.post(target_url, data=data_dict) #instead of sending GET request, send POST usings requests library
#data_dict stored as key value pairs
print(response.content)

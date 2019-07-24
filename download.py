#!/usr/bin/env python
import requests #http requests through python

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1] #split with / as delim -1 for last element in list
    #print(file_name)
    #print(get_response) #returns response object
    #print(get_response.content) #show content of response object
    with open(file_name, "wb") as out_file: #wb - open file for writing as binary
        out_file.write("test")
    
#download("https://rarlab.com/rar/wrar571.exe")
download("http://vulnweb.com/acunetix-logo.png")

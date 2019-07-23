#!/usr/bin/env python
import requests #http requests through python

def download(url):
    get_response = requests.get(url)
    print(get_response) #returns response object
    print(get_response.content) #show content of response object
    
download("https://rarlab.com/rar/wrar571.exe")

#!/usr/bin/env python
import requests #http requests through python

def download(url):
    get_response = requests.get(url)
    print(get_response)
    
download("https://rarlab.com/rar/wrar571.exe")

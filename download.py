#!/usr/bin/env python
import requests #http requests through python

def download(url):
    get_request = requests.get(url)
    print(get_request)
    
download("https://rarlab.com/rar/wrar571.exe")

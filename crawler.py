#!/usr/bin/env python

import requests

def request(url):
    try:
        return requests.get("http://" + url)
        print(get_response)
    except requests.exceptions.ConnectionError:
        #this is the type of error pythong returns if it encounters an issue querying the url
        print("Error, check url")
        pass
    
try:
    subdomains_list = raw_input("Enter exact path of word list for subdomains: ")
except:
    print("File location not found, check path")
    
with open(subdomains_list, "r") as wordlist_file:
    for line in wordlist_file:
        print(line)
        

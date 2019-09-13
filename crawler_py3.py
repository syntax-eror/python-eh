#!/usr/bin/env python 3

import requests

def request(url):
    try:
        return requests.get("http://" + url)
        print(get_response)
    except requests.exceptions.ConnectionError:
        #this is the type of error pythong returns if it encounters an issue querying the url
        print("Error, check url")
        pass
    
subdomains_list = input("Enter exact path of word list for subdomains: ")
#location of wordlist file containing subdomains to check

target_url = "google.com"
try:
    with open(subdomains_list, "r") as wordlist_file:
        for line in wordlist_file:
            test_url = line + target_url
            print(test_url)
except:
    print("File not found, check path and filename")

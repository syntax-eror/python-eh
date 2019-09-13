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
    
subdomains_list = raw_input("Enter exact path of word list for subdomains: ")
#location of wordlist file containing subdomains to check

target_url = raw_input("Enter domain: ")

try:
    with open(subdomains_list, "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip() #strip - built in method to work with strings; removes whitespace
            #so Line1
            test_url = word + "." + target_url #find subdomain, eg word.google.com
            response = request(test_url)
            if response:
                print("[+] Found subdomain: " + test_url)
except:
    print("File not found, check path and filename")

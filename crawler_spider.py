#!/usr/bin/env python

import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        #this is the type of error python returns if it encounters an issue querying the url
        #print("Error, check url")
        pass

target_url = raw_input("Enter domain: ")

response = request(target_url)

href_links = re.findall('(?:href=")(.*)"') #?: - non-matching

print(response.content) #.content is a method of response that will return the content of the request from requests library

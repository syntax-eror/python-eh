#!/usr/bin/env python

import re, requests

target_url = raw_input("Enter domain: ")

def extract_links(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

href_links = extract_links(target_url)
for link in href_links:
    print(link)
    
#commented code:
#==================================
#def request(url):
    #try:
        #return requests.get("http://" + url)
    #except requests.exceptions.ConnectionError:
        #this is the type of error python returns if it encounters an issue querying the url
        #print("Error, check url")
        #pass
        
target_url = raw_input("Enter domain: ")

#response = request(target_url)


def extract_links(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)
    #regex to find all part of a href tag, up to the last double quote <a href="https://example.com/subdir/">
    #split into two groups with () - href part of the expression is placed in different group
    #?: - non-matching - make href part non-matching
    #? - make group non-greedy - will match up until first double quote it finds after the opening "

#print(response.content) #.content is a method of response that will return the content of the request from requests library
href_links = extract_links(target_url)
print(href_links)

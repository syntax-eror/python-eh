#!/usr/bin/env python

import re, requests, urlparse

target_url = raw_input("Enter domain: ")
target_links = [] #initialize empty list

def extract_links(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

def crawl(url):
    href_links = extract_links(url)
    for link in href_links:
        link = urlparse.urljoin(url, link) #urlparse is library that will take relative links and convert to full links
        #this converts relative links like /onpage/ to full links https://example.com/onpage

        if "#" in link: #if relative link that redirects to another part of same page (ex: ex.com/#about)
            link = link.split("#")[0] #split link into two elements, 0 - first index - everything before #

        if target_url in link and link not in target_links: #if not an external link and not already added to list
            target_links.append(link)
            print(link)
            crawl(link) #recursive - calls itself
 
 crawl(target_url)
 
 
 



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

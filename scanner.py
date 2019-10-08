#!/usr/bin/env python

import re, requests, urlparse

class Scanner:
    def __init__(self, url):
        self.session = requests.Session() #set up session object
        #this enables established sessions to be used rather than individual requests;
        #allows use of webpages that require login
        self.target_url = url
        self.target_links = []
        
    def extract_links(self, url):
        response = self.session.get(url)
        return re.findall('(?:href=")(.*?)"', response.content)
    
    def crawl(self, url=None): #specify default value for URL;
        #allows crawl method to be called without passing a url
        if url == None: #url will equal None if method is called from outside;
            #function
            url = self.target_url #if this is the case, set it to target_url
        href_links = self.extract_links(url)
        for link in href_links:
            link = urlparse.urljoin(url, link) #urlparse is library that will take relative links and convert to full links
            #this converts relative links like /onpage/ to full links https://example.com/onpage
            
            if "#" in link: #if relative link that redirects to another part of same page (ex: ex.com/#about)
                link = link.split("#")[0] #split link into two elements, 0 - first index - everything before #
                
            if self.target_url in link and link not in self.target_links: #if not an external link and not already added to list
                self.target_links.append(link)
                print(link)
                self.crawl(link) #recursive function to continue checking each page on site for addiitional links

#!/usr/bin/env python

import re, requests, urlparse

class Scanner:
    def __init__(self, url):
        self.target_url = url
        self.target_links = []
        
    def extract_links(self, url):
        response = requests.get(url)
        return re.findall('(?:href=")(.*?)"', response.content)
    
    def crawl(self, url):
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

#!/usr/bin/env python

#class to be imported and used with vulnerability_scanner.py

import re, requests, urlparse
from BeautifulSoup import BeautifulSoup

class Scanner:
    def __init__(self, url, links_to_ignore):
        self.session = requests.Session() #set up session object
        #this enables established sessions to be used rather than individual requests;
        #allows use of webpages that require login, eg, dvwa/login.php to allow crawler to login
        self.target_url = url
        self.target_links = []
        self.links_to_ignore = links_to_ignore #pass in list of links to not scan from vulnscanner.py
        #these links will then be excluded in the crawler function below
        
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
                
            if self.target_url in link and link not in self.target_links and link not in self.links_to_ignore: 
                #if not an external link and not already added to list and not in list to not crawl;
                #don't crawl logout pages, etc
                self.target_links.append(link)
                print(link)
                self.crawl(link) #recursive function to continue checking each page on site for addiitional links
                
    def extract_forms(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content, features="lxml")
        return parsed_html.findAll("form") #substitute form with any element you want to locate on page, ie "blockquote"
    
    def submit_form(self, form, value, url):
        action = form.get("action") #"action" is the name of the HTML attribute for specifying what page should do
        #i.e, form id="lookup" action="index.php?page=target-page.php"
        method = form.get("method") #same thing for method tag in code of web page
        post_url = urlparse.urljoin(url, action) #join two urls; 10.0.0.1 + index.php?page=target-page.php
        #10.0.0.1/index.php-etc
        #print(action)
        #print(method)
        input_list = form.findAll("input") #same as forms_list, taking all elements of "input" on page and storing in a list (dict)
        post_data = {}
        for input in input_list:
            input_name = input.get("name")
            input_type = input.get("type")
            #print(input_name)
            input_value = input.get("value")
            if input_type == "text": #if input is not a button or other object, just text
                input_value = value
                
            post_data[input_name] = input_value
            
        if method == "post":
            return self.session.post(post_url, data=post_data)
        return self.session.get(post_url, params=post_data)

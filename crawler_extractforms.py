#!/usr/bin/env python

from bs4 import BeautifulSoup #pip install beautifulsoup4 if needed
#module that allows parsing of HTML - can more easily extract specific elements from pages than using regex
import requests
import urlparse

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

url = raw_input("Enter target URL: ")
response = request(url)

parsed_html = BeautifulSoup(response.content, features="lxml")
forms_list = parsed_html.findAll("form") #substitute form with any element you want to locate on page, ie "blockquote"

for form in forms_list:
    action = form.get("action") #"action" is the name of the HTML attribute for specifying what page should do
    #i.e, form id="lookup" action="index.php?page=target-page.php"
    method = form.get("method") #same thing for method tag in code of web page
    post_url = urlparse.urljoin(target_url, action) #join two urls; 10.0.0.1 + index.php?page=target-page.php
    #10.0.0.1/index.php-etc
    print(action)
    print(method)
    
    input_list = form.findAll("input") #same as forms_list, taking all elements of "input" on page and storing in a list (dict)
    for input in input_list:
        input_name = input.get("name")
        print(input_name)

#print(forms_list[0])

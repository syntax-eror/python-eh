#!/usr/bin/env python

from bs4 import BeautifulSoup #pip install beautifulsoup4 if needed
#module that allows parsing of HTML - can more easily extract specific elements from pages than using regex
import requests

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
    action = form.get("action") #"action" is the name of the tag in the HTML for specifying what page should do
    #i.e, form id="lookup" action="index.php?page=target-page.php"
    print(action)

#print(forms_list[0])

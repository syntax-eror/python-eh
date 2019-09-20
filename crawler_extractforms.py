#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

url = raw_input("Enter target URL: ")
response = request(url)
print(response.content)

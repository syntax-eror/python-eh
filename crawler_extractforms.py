#!/usr/bin/env python

from bs4 import BeautifulSoup #pip install beautifulsoup4 if needed
import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

url = raw_input("Enter target URL: ")
response = request(url)
print(response.content)

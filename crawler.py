#!/usr/bin/env python

import requests

url = "google.com"

try:
    get_response = requests.get("http://" + url)
    print(get_response)
except requests.exceptions.ConnectionError:
    print("Error, check url")
    pass

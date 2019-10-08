#!/usr/bin/env python

import requests, scanner

target_url = "http://10.0.2.4/dvwa/"
data_dict = {"username": "admin", "password": "password", "Login": "submit"}
response = requests.post(target_url, data=data_dict)

vuln_scan = scanner.Scanner(target_url)
response = vuln_scan.session.post(target_url, data=data_dict)
vuln_scan.crawl() #can pass it with no arguments if you use updated scanner.py
#see documentation within scanner.py

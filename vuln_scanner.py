#!/usr/bin/env python

import requests, scanner

target_url = "http://10.0.2.4/dvwa/"
links_to_ignore = ["http://10.0.2.4/dvwa/logout.php"] #create list of links to not scan, i.e., logout pages
data_dict = {"username": "admin", "password": "password", "Login": "submit"}

vuln_scan = scanner.Scanner(target_url, links_to_ignore) #establishes session using connection method in;
#scanner.py - this allows use on pages with login forms as opposed to sending invidiual;
#get and post requests

vuln_scan.session.post("http://10.0.2.20/dvwa/login.php", data=data_dict)

vuln_scan.crawl() #can pass it with no arguments if you use updated scanner.py
#see documentation within scanner.py

#response = vuln_scan.session.post(target_url, data=data_dict)
#response = requests.post(target_url, data=data_dict)

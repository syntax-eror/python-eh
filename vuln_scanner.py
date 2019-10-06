#!/usr/bin/env python

import scanner

target_url = "http://10.0.2.4/mutillidae/"
vuln_scan = scanner.Scanner(target_url)
vuln_scan.crawl() #can pass it with no arguments if you use updated scanner.py
#see documentation within scanner.py

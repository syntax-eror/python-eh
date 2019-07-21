#!/usr/bin/env python

import subprocess, smtplib

def send_email(email, password, message):

command = "msg * Test Message"
subprocess.Popen(command, shell=True)

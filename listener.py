#!/usr/bin/env python3

import socket

listen_ip = input("Enter IP Address to listen on: ")
listen_port = input("Enter port to listen on: ")

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#setsockopt = method for setting socket options
#(level, attribute, value)
#this allows reuse of sockets, so they will persist through lost connection
listener.bind((listen_ip, listen_port))
listener.listen(0) #specify backlog - number of connections that can be queued before it resets
listener.accept() #needed to allow connection on the specified IP and port

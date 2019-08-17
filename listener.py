#!/usr/bin/env python3

import socket

listen_ip = input("Enter IP Address to listen on: ")
listen_port = int(input("Enter port to listen on: "))

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#setsockopt = method for setting socket options
#(level, attribute, value)
#this allows reuse of sockets, so they will persist through lost connection

listener.bind((listen_ip, listen_port))
listener.listen(0) #specify backlog - number of connections that can be queued before it resets
print("[+] Listening for incoming connections on ", listen_ip, "Port:", listen_port)
#listener.accept() - needed to allow connection on the specified IP and port

#listener.accept - the accept method of the socket method returns two values:
connection, address = listener.accept()
#first value - "connection" - socket object representing connection used to send or receive data
#second value - "addresss" - address bound to the connection

print("[+] Connection established from", str(address))

while True:
    command = input(">> ")
    connection.send(command) #this will return TypeError in python3; requires bytes-like object, not string
    result = connection.recv(1024) #receive result in 1024-byte chunks
    print(result)

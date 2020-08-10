#basic portscanner

import socket

def scan_port(ip, port):
    s = socket.socket() #create socket object
    scan_result = s.connect_ex((ip, port)) #returns 1 if successful, otherwise returns errno var
    return scan_result

try:
    ip = input("Enter IP or hostname to scan: ")
    port = int(input("Enter port to try: "))
    portscan_result = scan_port(ip, port)
    
    if portscan_result == 0:
        print("Port", port, "is open")
    else:
        print("Port", port, "is NOT open")
accept: #
    print("Something went wrong")

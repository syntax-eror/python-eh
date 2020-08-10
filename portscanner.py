#basic portscanner

import socket

s = socket.socket()

result = s.connect_ex(('IP',port))

if (result == 0):
    print('Port open')
else:
    print('Port not open')

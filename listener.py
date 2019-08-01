#!/usr/bin/env python3

import socket

listener = socket.socketsocket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #set socket option method
#(level, option, value)
#reuse sockets - persist through lost connection

listener.bind(("10.0.2.13"))

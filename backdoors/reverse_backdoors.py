#!/user/bin/env python
import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.146.147", 1337))

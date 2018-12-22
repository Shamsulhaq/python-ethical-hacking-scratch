#!/user/bin/env python
import socket


listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind("192.168.146.148", 1337)
listener.listen(0)
print("\nWaitig for incoming connection.\n")
listener.accept()
print("\nGor a connection.\n")
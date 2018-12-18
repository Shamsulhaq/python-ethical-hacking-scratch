#!/user/bin/env python
import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.146.148", 1337))

connection.send("\n[+] connection established.\n".encode())

receive_data = connection.recv(1024)
print(receive_data)

connection.close()

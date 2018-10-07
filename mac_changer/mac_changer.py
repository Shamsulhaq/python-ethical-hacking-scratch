# !/user/bin/python3
import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change mack address. Example- eth0, wlan0")
parser.parse_args()

interface = input("interface > ")
set_mac = input("set Mac > ")

subprocess.run(["ifconfig", interface, "down"])
subprocess.run(["ifconfig", interface, "hw", "ether", set_mac])
subprocess.run(["ifconfig", interface, "up"])

print("[+] Change MAC address " + interface + "to" + set_mac)

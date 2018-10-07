# !/user/bin/python3
import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change mack address. Example- eth0, wlan0")
parser.add_option("-m", "--mac", dest="set_mac", help="Set MAC address. Example '00:11:22:33:44:55'."
                                                      "Make sure it will 12 characters")
(options, argument) = parser.parse_args()

interface = options.interface or input("interface > ")
set_mac = options.set_mac or input("set Mac > ")

# interface = input("interface > ")
# set_mac = input("set Mac > ")

subprocess.run(["ifconfig", interface, "down"])
subprocess.run(["ifconfig", interface, "hw", "ether", set_mac])
subprocess.run(["ifconfig", interface, "up"])

print("[+] Change MAC address " + interface + " to " + set_mac)

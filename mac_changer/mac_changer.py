# !/user/bin/python3
import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change mack address. Example- eth0, wlan0")
    parser.add_option("-m", "--mac", dest="set_mac", help="Set MAC address. sure it will 12 characters")
    # return parser.parse_args()
    (options, argument) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.set_mac:
        parser.error("[-] Please specify new mac, use --help for more info")
    return options


def change_mac(interface, set_mac):
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", set_mac])
    subprocess.run(["ifconfig", interface, "up"])

    print("[+] Change MAC address " + interface + " to " + set_mac)


options = get_arguments()
# interface = options.interface or input("interface > ")
# set_mac = options.set_mac or input("mack > ")

interface = options.interface
set_mac = options.set_mac

print([interface, set_mac])
# change_mac(interface, set_mac)


result_checking = subprocess.check_output(["ifconfig", options.interface], stderr=subprocess.STDOUT, shell=True)
print(result_checking)

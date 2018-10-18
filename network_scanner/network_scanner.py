# !/user/bin/python
from scapy import all as scapy

"""
    pdst = 
    psrc = ip address
    hwsrc = hardware / mac address
"""


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_request = broadcast/arp_request
    answered_list = scapy.srp(arp_broadcast_request, timeout=1, verbose=False)[0]

    print('\nSCANNING RESULT')
    print('-'*50, "\nIP\t\t\tMAC ADDRESS")
    print('-'*50)

    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)


scan("192.168.31.1/24")

# !/user/bin/python
from scapy import all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_request = broadcast/arp_request
    print(arp_broadcast_request.summary())
    arp_broadcast_request.show()


scan("192.168.31.1/24")

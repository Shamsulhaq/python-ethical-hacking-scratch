# !/user/bin/python
from scapy import all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())


scan("192.168.31.1/24")

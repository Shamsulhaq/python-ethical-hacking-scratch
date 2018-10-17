# !/user/bin/python
from scapy import all as scapy


def scan(ip):
    scapy.arping(ip)


scan("192.168.31.1/24")

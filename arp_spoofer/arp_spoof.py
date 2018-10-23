# !/user/bin/python3
import scapy.all as scapy

paket = scapy.ARP(
    op=2, pdst="192.168.146.147",
    hwdst="fe80::20c:29ff:fee7:ccc9",
    psrc="192.168.31.1")




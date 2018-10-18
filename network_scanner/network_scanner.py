# !/user/bin/python
import argparse
from scapy import all as scapy


def get_arguments():
    parse = argparse.ArgumentParser()
    parse.add_argument("-t", "--target", dest="target", help="Target IP / IP range")
    option = parse.parse_args()
    if not option.target:
        parse.error("[-] Please specify your target IP and range. Use --help for more info")
    return option


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_request = broadcast/arp_request
    answered_list = scapy.srp(arp_broadcast_request, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list


def scanning_result(results):
    print('\nSCANNING RESULT:')
    print('-' * 50, "\nIP\t\t\tMAC ADDRESS")
    print('-' * 50)

    for client in results:
        print(client["ip"] + '\t\t' + client["mac"])
    print('\nScan Complete.\n')


option = get_arguments()
final_result = scan(option.target)
scanning_result(final_result)

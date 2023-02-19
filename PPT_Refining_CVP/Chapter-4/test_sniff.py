from scapy.all import sniff, conf
from scapy.layers.dot11 import Dot11Beacon, Dot11ProbeReq
from scapy.layers.inet import TCP
from scapy.layers.dns import DNS


def pkt_print(pkt):
    if pkt.haslayer(Dot11Beacon):
        print('[+] Detected 802.11 Beacon Frame')
    elif pkt.haslayer(Dot11ProbeReq):
        print('[+] Detected 802.11 Probe Request Frame')
    elif pkt.haslayer(TCP):
        print('[+] Detected a TCP Packet')
    elif pkt.haslayer(DNS):
        print('[+] Detected a DNS Packet')


if __name__ == '__main__':
    conf.iface = 'mon0'
    sniff(prn=pkt_print)


# The code is set to listen on a wireless interface named mon0. You may need to change the interface 
# name based on your setup. To check the available interfaces in your system, you can use the following 
# command in a terminal:

# ipconig for windows ifconfig for linux


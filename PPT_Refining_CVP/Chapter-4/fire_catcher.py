import re
import argparse
from scapy.layers.inet import IP
from scapy.all import sniff, conf


def fire_catcher(pkt):
    cookie_table = {}
    raw = pkt.sprintf('%Raw.load%')
    r = re.findall(r'wordpress_[0-9a-fA-F]{32}', raw)
    if r and 'Set' not in raw:
        if r[0] not in list(cookie_table.keys()):
            cookie_table[r[0]] = pkt.getlayer(IP).src
            print('[+] Detected and indexed cookie.')
        elif cookie_table[r[0]] != pkt.getlayer(IP).src:
            print(f'[*] Detected Conflict for {r[0]}')
            print(f'Victim   = {cookie_table[r[0]]}')
            print(f'Attacker = {pkt.getlayer(IP).src}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='python3 fire_catcher.py INTERFACE')
    parser.add_argument('iface', type=str, metavar='INTERFACE',
                        help='specify the interface to listen on')
    args = parser.parse_args()
    conf.iface = args.iface

    try:
        sniff(filter='tcp port 80', prn=fire_catcher)
    except KeyboardInterrupt:
        exit(0)



'''

The code defines a script fire_catcher that captures and analyzes packets transmitted over a specified 
network interface. The script makes use of the Python re (regular expression) module to detect a specific 
pattern in the payloads of HTTP traffic (i.e. traffic transmitted over port 80) that corresponds to a 
WordPress session cookie.

The fire_catcher function takes a single argument, a packet pkt, and analyzes its payload for the presence 
of a WordPress session cookie. If a cookie is detected, the function adds an entry to a dictionary 
cookie_table, where the cookie string is the key and the source IP address of the packet is the value. 
If a subsequent packet with the same cookie string but a different source IP address is detected, the 
function prints a message indicating a conflict between two entities claiming to have the same session.

The main section of the script uses the argparse module to parse the command line arguments passed to the 
script. The user must specify the network interface to listen on via the iface argument. The sniff function 
from the scapy library is used to capture packets and pass them to the fire_catcher function for analysis. 
The script listens indefinitely for packets until the user terminates the process with a keyboard interrupt 
(i.e. Ctrl-C).

'''
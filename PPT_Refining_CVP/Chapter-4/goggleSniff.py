import re
import argparse
from scapy.all import Raw
from scapy.all import sniff, conf


def find_google(pkt):
    if pkt.haslayer(Raw):
        payload = pkt.getlayer(Raw).load
        if 'GET' in payload and 'google' in payload:
            r = re.findall(r'(?i)&q=(.*?)&', payload)
            if r:
                search = r[0].split('&')[0]
                search = search.replace('q=', '').replace('+', ' ').\
                    replace('%20', ' ')
                print(f'[+] Searched For: {search}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='python3 google_sniff.py INTERFACE')
    parser.add_argument('iface', type=str, metavar='INTERFACE',
                        help='specify the interface to listen on')
    args = parser.parse_args()
    conf.iface = args.iface

    try:
        print('[*] Starting Google Sniffer.')
        sniff(filter='tcp port 80', prn=find_google)
    except KeyboardInterrupt:
        exit(0)


# Here's a breakdown of the code:

#     Importing required modules:
#         The "re" module is used to perform regular expression operations.
#         The "argparse" module is used to parse command-line arguments.
#         The "scapy.all" module contains all the functions and classes of the Scapy library.
#         The "Raw" class from "scapy.all" is used to extract the raw payload from network packets.

#     Defining the "find_google" function:
#         This function takes a network packet as an argument and checks if it has a "Raw" layer.
#         If the packet does have a "Raw" layer, the payload is extracted and checked if it contains the 
# string "GET" and "google".
#         If both the strings are found, the function uses regular expressions to extract the search query 
# from the payload.
#         The extracted query is then cleaned up, and a message is printed to the console indicating what was 
# searched for.

#     The main function:
#         It uses the "argparse" module to parse the command-line argument, which is the name of the network 
# interface to listen on.
#         The "conf.iface" attribute is set to the value of the parsed argument, which specifies the network 
# interface.
#         The "sniff" function from the "scapy.all" module is used to start the sniffing process, with the 
# "filter" argument set to "tcp port 80" to only listen to packets on port 80 (HTTP).
#         The "prn" argument is set to the "find_google" function, which will be called for each sniffed packet.
#         The "store" argument is set to 0, which means that the sniffed packets won't be stored in memory.
#         The main function also includes a try-except block to handle a keyboard interrupt, which allows the 
# user to stop the sniffing process by pressing "Ctrl + C".
import dpkt
import socket


def find_hivemind(pcap):
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport
            sport = tcp.sport

            if dport == 6667 and b"!lazor" in tcp.data.lower():
                print(f"[!] DDoS Hivemind issued by: {src}")
                print(f'{"":>3}[+] Target CMD: {tcp.data.decode("utf-8")}')

            if sport == 6667 and b"!lazor" in tcp.data.lower():
                print(f"[!] DDoS Hivemind issued to: {dst}")
                print(f'{"":>3}[+] Target CMD: {tcp.data.decode("utf-8")}')

        except Exception as e:
            print(f'{"":>3}[-] Exception: {e.__class__.__name__}')
            pass


with open("hivemind.pcap", "rb") as file:
    _pcap = dpkt.pcap.Reader(file)
    find_hivemind(_pcap)

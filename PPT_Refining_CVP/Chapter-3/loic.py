import dpkt
import socket


def find_download(pcap):
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            tcp = ip.data
            http = dpkt.http.Request(tcp.data)

            if http.method == 'GET':
                uri = http.uri.lower()
                if '.zip' in uri and 'loic' in uri:
                    print(f'[!] {src} downloaded LOIC.')

        except Exception as e:
            print(f'[-] Exception: {e.__class__.__name__}')
            pass

with open('download.pcap', 'rb') as file:
    _pcap = dpkt.pcap.Reader(file)
    find_download(_pcap)
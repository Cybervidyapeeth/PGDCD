import dpkt
import socket
import pygeoip
import argparse

gi = pygeoip.GeoIP('GeoLiteCity.dat')

def retGeoStr(ip):
   try:
       rec = gi.record_by_name(ip)
       city = rec['city']
       country = rec['country_code3']
       if city != " ":
          geoLoc = city+" , "+country
       else:
          geoLoc = country
       return geoLoc
   except:
       return "Unregistered"

def printPcap(pcap):
   for (ts,buf) in pcap:
       try:
           eth = dpkt.ethernet.Ethernet(buf)
           ip = eth.data
           src = socket.inet_ntoa(ip.src)
           dst = socket.inet_ntoa(ip.dst)
           print("[+] Src: "+src+"--> Dst: "+dst)
           print("[+] Src: "+retGeoStr(src)+"--> Dst: "+ retGeoStr(dst))
       except:
           pass

def main():
    parser = argparse.ArgumentParser(description='usage%prog -p <pcap file>')
    parser.add_argument('-p', dest='pcapFile', type=str, help='specify pcap filename')
    args = parser.parse_args()

    if args.pcapFile is None:
        print(parser.print_help())
        exit(0)
    pcapFile = args.pcapFile
    with open(pcapFile,'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        printPcap(pcap)

if __name__=='__main__':
    main()

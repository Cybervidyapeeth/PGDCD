import socket
import os
import sys


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except socket.timeout:
        print(f"[-] Timeout for {ip}:{port}")
    except ConnectionRefusedError:
        print(f"[-] Connection refused for {ip}:{port}")
    except Exception as e:
        print(f"[-] Error: {e}")
        return


def checkVulns(banner, filename):
    f = open(filename, "r", encoding="utf-8")
    for line in f.readlines():
        if line.strip("\n") in banner:
            print("[+] Server is vulnerable" + banner.strip("\n"))


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("[-] " + filename + " does not exist.")

        if not os.access(filename, os.R_OK):
            print("[-] " + filename + " access denied.")

        else:
            print("[-] Usage: <vuln filename>")
            portList = [21, 22, 25, 80, 110, 443]
            for x in range(147, 150):
                ip = "192.168.95." + str(x)

                for port in portList:
                    banner = retBanner(ip, port)
                    if banner:
                        print("[+] " + ip + ":" + banner)
                        checkVulns(banner, filename)


if __name__ == "__main__":
    main()

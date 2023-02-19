import dpkt, socket, pygeoip, argparse

gi = pygeoip.GeoIP("GeoLiteCity.dat")

def retGeoStr(ip):
    try:
        rec = gi.record_by_name(ip)
        city = rec['city']
        country = rec['country_code3']
        if city:
            geoLoc = city+", "+country
        else:
            geoLoc = country
        return geoLoc
    except:
        return "Unregistered"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the geolocation of an IP address")
    parser.add_argument("-i", "--ip", dest="ip", help="IP address to geolocate")
    args = parser.parse_args()
    if args.ip:
        print(retGeoStr(args.ip))
    else:
        print("[-] Please provide an IP address to geolocate.")

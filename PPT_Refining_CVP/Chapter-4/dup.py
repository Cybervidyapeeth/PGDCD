from scapy.layers.dot11 import RadioTap, Dot11
from scapy.layers.l2 import SNAP, LLC
from scapy.layers.inet import IP, UDP


def dup_radio(pkt):
    r_pkt = pkt.getlayer(RadioTap)
    version = r_pkt.version
    pad = r_pkt.pad
    present = r_pkt.present
    notdecoded = r_pkt.notdecoded
    n_pkt = RadioTap(version=version, pad=pad, present=present,
                     notdecoded=notdecoded)
    return n_pkt


def dup_dot11(pkt):
    d_pkt = pkt.getlayer(Dot11)
    subtype = d_pkt.subtype
    _type = d_pkt.type
    proto = d_pkt.proto
    fc_field = d_pkt.FCfield
    _id = d_pkt.ID
    addr1 = d_pkt.addr1
    addr2 = d_pkt.addr2
    addr3 = d_pkt.addr3
    sc = d_pkt.SC
    addr4 = d_pkt.addr4
    n_pkt = Dot11(subtype=subtype, type=_type, proto=proto, FCfield=fc_field,
                  ID=_id, addr1=addr1, addr2=addr2, addr3=addr3, SC=sc,
                  addr4=addr4)
    return n_pkt


def dup_snap(pkt):
    s_pkt = pkt.getlayer(SNAP)
    oui = s_pkt.OUI
    code = s_pkt.code
    n_pkt = SNAP(OUI=oui, code=code)
    return n_pkt


def dup_LLC(pkt):
    l_pkt = pkt.getlayer(LLC)
    dsap = l_pkt.dsap
    ssap = l_pkt.ssap
    ctrl = l_pkt.ctrl
    n_pkt = LLC(dsap=dsap, ssap=ssap, ctrl=ctrl)
    return n_pkt


def dup_IL(pkt):
    i_pkt = pkt.getlayer(IP)
    version = i_pkt.version
    tos = i_pkt.tos
    _id = i_pkt.id
    flags = i_pkt.flags
    ttl = i_pkt.ttl
    proto = i_pkt.proto
    src = i_pkt.src
    dst = i_pkt.dst
    options = i_pkt.options
    n_pkt = IP(version=version, id=_id, tos=tos, flags=flags, ttl=ttl,
               proto=proto, src=src, dst=dst, options=options)
    return n_pkt

def dup_UDP(pkt):
    u_pkt = pkt.getlayer(UDP)
    sport = u_pkt.sport
    dport = u_pkt.dport
    n_pkt = UDP(sport=sport, dport=dport)
    return n_pkt



'''
The code defines several functions, each of which duplicates a specific layer of a packet:

    dup_radio: This function duplicates the RadioTap layer of the packet. It retrieves the RadioTap layer 
    from the packet using the getlayer method and then creates a new RadioTap object with the same version, 
    pad, present, and notdecoded values.

    dup_dot11: This function duplicates the Dot11 layer of the packet. It retrieves the Dot11 layer from the 
    packet using the getlayer method and then creates a new Dot11 object with the same subtype, type, proto, 
    FCfield, ID, addr1, addr2, addr3, SC, and addr4 values.

    dup_snap: This function duplicates the SNAP layer of the packet. It retrieves the SNAP layer from the 
    packet using the getlayer method and then creates a new SNAP object with the same OUI and code values.

    dup_LLC: This function duplicates the LLC layer of the packet. It retrieves the LLC layer from the 
    packet using the getlayer method and then creates a new LLC object with the same dsap, ssap, and ctrl 
    values.

    dup_IL: This function duplicates the IP layer of the packet. It retrieves the IP layer from the packet 
    using the getlayer method and then creates a new IP object with the same version, tos, id, flags, ttl, 
    proto, src, dst, and options values.

    dup_UDP: This function duplicates the UDP layer of the packet. It retrieves the UDP layer from the 
    packet using the getlayer method and then creates a new UDP object with the same sport and dport values.

These functions can be used to duplicate individual layers of a packet, allowing the user to modify or 
inspect specific layers without affecting the original packet.
'''
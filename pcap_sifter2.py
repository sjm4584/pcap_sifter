#! /usr/bin/env python
from scapy.all import *
import re, sys, argparse


sqli_regex = ".*\'.*|[0-9]\=|\'[0-9].*" #this is great if we weren\'t dealing with web encoded data :(
we_sqli_regex = ".*\%.*|[0-9]\=|\%[0-9].*" #this same as above but for WebEncoded data :)

reader = PcapReader('capture1.pcap')


#For each packet in capture extract the payload and see if it's flagged by our regex
for p in reader:
	pkt = p.payload
	load = pkt.payload.payload

	match = re.search(we_sqli_regex, str(load))
	if match:
		print "-------- MATCH FOUND -------"
		print load
	else:
		continue


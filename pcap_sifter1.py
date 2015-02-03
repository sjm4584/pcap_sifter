#! /usr/bin/env python
from scapy.all import *
import re, sys, argparse, MySQLdb

#install MySQLdb from apt-get or pip. Create a db called "exploitdb" and a table "sqli" with your exploits
#or modify this code to fit your own database structure! I should make it cmdline args but time...


#conect to mysql and create a db obj so we can run query to grab all strings to compare to
db = MySQLdb.connect(host="localhost", user="mysqluser", passwd="", db="exploitdb")
cur = db.cursor()

cur.execute("SELECT * FROM sqli")
exploits = cur.fetchall()

reader = PcapReader('capture1.pcap') 

#for each packet payload check it against our db of attack strings
for p in reader:
	pkt = p.payload
	load = pkt.payload.payload 
	
	for row in exploits:
		sploit = row[0]
		m = re.search(str(sploit), str(load))
		if m:
			print "[+] FOUND: \t "+sploit
		else:
			continue

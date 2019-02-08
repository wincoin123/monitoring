import sys
import re
import datetime

logfile = "D:/test_log.txt"

file = open(logfile, "r")
ips = {}

strptime = datetime.datetime.strptime
for text in file.readlines():
    text = text.rstrip()
    found = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',text)
    match = text.partition('[')[-1].rpartition(']')[0]
    if found and match:
        ips[match]=found            
for ip in ips:
    outfile = open("D:/updates.txt", "a")
    attacker = "".join(ips[ip][0])
    if len(ips[ip]) > 1:
        server = "".join(ips[ip][1])
    if attacker is not '':
        print ("Request from: %s" % (attacker))
        outfile.write(attacker)
        outfile.write("@")
        outfile.write(ip)
        attacker = ''
        if server is not '':
            print (" to : %s" % (server))
            server=''
        print (" @ %s" % (ip))
        outfile.write("\n")

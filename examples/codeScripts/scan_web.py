#!/usr/bin/python
'''scan web begin...'''
import sys,httplib
from optparse import OptionParser
usageString = "Usage: %prog [options] hostname"
parser = OptionParser(usage=usageString)
(opts,args) = parser.parse_args()
if len(args) < 1:
    parser.error("Hostname is required")
print __doc__
website = args[0]
#login path
dirs = ["admin","login","admin_index","admin/admin","admin/login","admin/index","admin/user"]
for line in dirs:
    conn = httplib.HTTPConnection(website)
    conn.request('GET','/'+line)
    r1 = conn.getresponse()
    if r1.status == 200 or r1.status == 301:
        print '\033[;32m' + website+'/'+line,r1.status,r1.reason + '\033[0m'
    else:
        print website+'/'+line,r1.status,r1.reason
    conn.close()
    conn = httplib.HTTPConnection(website)
    conn.request('GET','/'+line+'.asp')
    r1 = conn.getresponse()
    if r1.status == 200 or r1.status == 301:
        print '\033[;32m' + website+'/'+line+'.asp',r1.status,r1.reason + '\033[0m'
    else:
        print  website+'/'+line+'.asp',r1.status,r1.reason   
    conn.close()
    conn = httplib.HTTPConnection(website)
    conn.request('GET','/'+line+'.php')
    r1 = conn.getresponse()
    if r1.status == 200 or r1.status == 301:
        print '\033[;32m' + website+'/'+line+'.php',r1.status,r1.reason + '\033[0m'
    else:
        print website+'/'+line+'.php',r1.status,r1.reason
    conn.close()

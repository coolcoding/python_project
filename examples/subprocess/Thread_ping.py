#!/usr/bin/env python

from threading import Thread
import subprocess
from Queue import Queue


num_threads = 3
queue = Queue()
ips = ['192.168.56.200','192.168.56.201']
def pinger(i,q):
    while True:
        ip = q.get()
        print 'Thread %s:Pinging %s' % (i,ip)
        ret = subprocess.call('ping -c 1 %s' % ip,
                            shell=True,
                            stdout = open('/dev/null'),
                            stderr = subprocess.STDOUT)
        if ret == 0:
            print '\033[;32m%s:is alive\033[0m' % ip
        else:
            print '\033[;31m%s:did not repond\033[0m' % ip
        q.tast_done()


for i in range(num_threads):
    woker = Thread(target=pinger,args=(i,queue))
    woker.setDaemon(True)
    woker.start()

for ip in ips:
    queue.put(ip)
    print 'Main Thread waiting'
    queue.join()
    print 'Done'

#!pyenv/bin/python
import re
import time
import inspect
import urllib2
import json
import socket

class getMonitorInfo():

    def getTime(self):
        return str(int(time.time()) + 8 * 3600)

    def getHost(self):
        return socket.gethostname()

    def getMemTotal(self):
        with open('/proc/meminfo') as men_total:
            a = int(men_total.readline().split()[1])
            return  a/1024


    def getMemFree(self,noBufferCache=True):
        if noBufferCache:
            with open('/proc/meminfo') as men_open:
                T = int(men_open.readline().split()[1])
                F = int(men_open.readline().split()[1])
                B = int(men_open.readline().split()[1])
                C = int(men_open.readline().split()[1])
                return (F+B+C)/1024
        else:
            with open('/proc/meminfo') as men_open:
                T = men_open.readline()
                return T/1024

    def getLoadAvg(self):
        with open('/proc/loadavg') as loadavg_open:
            lo = loadavg_open.read().split()[:3]
            return ','.join(lo)

    def getMemUsage(self,noBufferCache=True):
        if noBufferCache:
            with open('/proc/meminfo') as men_open:
                T = int(men_open.readline().split()[1])
                F = int(men_open.readline().split()[1])
                B = int(men_open.readline().split()[1])
                C = int(men_open.readline().split()[1])
                return (T-F-B-C)/1024
        else:
            with open('/proc/meminfo') as men_open:
                T = int(men_open.readline().split()[1])
                F = int(men_open.readline().split()[1])
                return (T-F)/1024



    def runAllGet(self):
        data = {}
        for func in inspect.getmembers(self,predicate=inspect.ismethod):
            if func[0][:3] == 'get':
                data[func[0][3:]] = func[1]()

        return data

if __name__ == '__main__':
    men = getMonitorInfo()
    while True:
        data = men.runAllGet()
        print data
        req = urllib2.Request("http://127.0.0.1:8888",json.dumps(data),{'Content-Type': 'application/json'})
        f = urllib2.urlopen(req)
        response = f.read()
        f.close()
        time.sleep(120)

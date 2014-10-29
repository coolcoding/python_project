#!/usr/bin/env python
import sys
logfile = sys.argv[1]
def ClientCache(logfile_path):
        contents = open(logfile, "r")
        totalrequests = 0
        cacherequests = 0
        for line in contents:
                totalrequests += 1
                if line.split(" ")[8] == "304":
                        cacherequests += 1
    print "Percentage of requests that were client-cached: ", str(cacherequests) + "%"
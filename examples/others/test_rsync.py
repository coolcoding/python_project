#!/usr/bin/env python

from subprocess import call

import sys

source = '/etc/'
dest = '/tmp'
rsync = 'rsync'
args = '-a'
cmd = '%s %s %s %s' % (rsync,args,source,dest)

def sync():
    ret = call(cmd,shell=True)
    if ret != 0:
        print 'rsync failed'
        sys.exit(1)

sync()

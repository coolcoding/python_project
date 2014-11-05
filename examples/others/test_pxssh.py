#!/usr/bin/env python

import pxssh
import getpass



hostname,username,passwd = ('192.168.56.200','root','toor')

try:
    s = pxssh.pxssh()
    s.login(hostname,username,passwd)
    s.sendline('uptime')
    s.prompt()
    print s.before
    s.sendline('df -h')
    s.prompt()
    print s.before
    s.logout()
except pxssh.ExceptionPxssh, e:
    print 'pxssh failed on login.'
    print str(e)

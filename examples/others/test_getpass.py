#!/usr/bin/env python
#coding:utf-8

import getpass

defaultpwd = '2222'
user = getpass.getuser()
print "Hello %s" % user
p = getpass.getpass("please type the password:")
if p == defaultpwd:
    print "welcome back to the system"
else:
    print 'error'

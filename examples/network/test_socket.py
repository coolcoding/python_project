#!/usr/bin/env python

import socket
import re
import sys




def check_serve(address,port):
    s = socket.socket()
    print "Attempting to connect to %s on port %s" % (address,port)
    try:
        s.connect((address,port))
        print "Connected to %s on port %s" % (address,port)
        return True
    except socket.error,e:
        print 'Connection to %s on port %d failed: %s' %  (address,port,e)
        return False


if __name__ == '__main__':
    from  optparse  import OptionParser
    parse = OptionParser()
    parse.add_option('-a','--address',dest='address',default='127.0.0.1',help='Address for server')
    parse.add_option('-p','--port',dest='port',type='int',default=80,help='port for server')
    (opt,args) = parse.parse_args()
    print 'options:%s,args:%s' % (opt,args)
    check = check_serve(opt.address,opt.port)
    print 'check server return %s'  %  check
    sys.exit(not check)

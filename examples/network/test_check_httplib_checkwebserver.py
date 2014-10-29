#!/usr/bin/env  python

import re
import httplib
import sys


def checkServer(address,port,resource):
    if not resource.startswith('/'):
        resource = '/' + resource
    try:
        conn = httplib.HTTPConnection(address,port)
        print 'HTTP connection created Successfully'
        req = conn.request('GET',resource)
        print 'request for %s Successful' % resource
        respose = conn.getresponse()
        print 'respose status:%s' % respose
    except sock.error,e:
        print 'HTTP connection Failed:%s' % e
        return False
    finally:
        conn.close()
        print 'HTTP connection closed Successful'
    if respose.status in [200,301]:
        return True
    else:
        return False
    
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-a','--address',dest='address',default='localhost',help='address for server')
    parser.add_option('-p','--port',dest='port',default='80',type='int',help='port for server')
    parser.add_option('-r','--resource',dest='resource',default='index.html',help='resource for server')
    (options,args) = parser.parse_args()
    print 'options:%s,args:%s' % (options,args)
    check = checkServer(options.address,options.port,options.resource)
    print 'check server return %s' % check
    sys.exit(not check)

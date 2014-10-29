#!/usr/bin/env python

import socket
import re
import sys

def check_webserver(address,port,resource):
    #build up http request string 
    if not resource.startswith('/'):
        resource = '/' + resource
    request_string = 'GET %s HTTP/1.1\r\nHost:%s\r\n\r\n' % (resource,address)
    print 'HTTP:request:'
    print '|||%s|||' % request_string
    #create a tcp socket
    s = socket.socket()
    print 'Attempt to connect to %s on port %s' %  (address,port)
    try:
        s.connect((address,port))
        print 'Connected to %s on port %s' % (address,port)
        s.send(request_string)
        #only need 100 bye
        rsp = s.recv(100)
        print 'Received 100 bytes of HTTP respose'
        print '|||%s|||' % rsp
    except socket.error,e:
        print 'Connetion to %s on port %s failed: %s' % (address,port,e)
        return False
    finally:
        #close connetion
        print 'closing the connction'
        s.close()
    lines = rsp.splitlines()
    print 'First line of HTTP respose:%s' % lines[0]
    try:
        version,status,message = re.split(r'\s',lines[0],2)
        print 'Version:%s,Status:%s,Message:%s' %  (version,status,message)
    except ValueError:
        print 'Failed to split status line'
        return False
    if status in ['200','301']:
        print 'Success - status was %s' % status
    else:
        print 'Status was %s' % status
        return False



if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-a','--address',dest='address',default='localhost',help='address for server')
    parser.add_option('-p','--port',dest='port',default='80',type='int',help='port for server')
    parser.add_option('-r','--resource',dest='resource',default='index.html',help='RESOURCE to check')
    (options,args) = parser.parse_args()
    print 'options:%s,args:%s' % (options,args)
    check = check_webserver(options.address,options.port,options.resource)
    print 'check webserver returned %s' % check
    sys.exit(not check)

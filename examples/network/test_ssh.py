#!/usr/bin/env python

import paramiko

if __name__ == '__main__':
    from  optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-l','--hostname',dest='hostname',default='localhost',help='host for server')
    parser.add_option('-u','--username',dest='username',default='root',help='username for server')
    parser.add_option('-w','--passwd',dest='passwd',default='root',help='password for server')
    parser.add_option('-p','--port',dest='port',type='int',default='22',help='port for server')
    (options,args) = parser.parse_args()
    print 'options:%s,args:%s' % (options,args)
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_host_keys('/root/.ssh/known_hosts')
    s.connect(options.hostname,options.port,options.username,options.passwd)
    stdin,stdout,stderr = s.exec_command('ifconfig')
    print stdout.read()
    s.close()

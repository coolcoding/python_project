#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import sys
import pexpect

#print run('ls').strip()

def ssh_cmd(ip,user,passwd,cmd):
    ret = -1
    ssh = pexpect.spawn('ssh root@%s "%s"' % (ip,cmd))
    try:
        i = ssh.expect(['password', 'Are you sure you want to continue connecting'], timeout=5)
        print ssh.before
        print ssh.after
        if i == 0:
            ssh.sendline(passwd)
        elif i == 1:
            ssh.sendline('yes\n')
            ssh.expect('password:')
            ssh.sendline(passwd)
        ssh.sendline(cmd)
        r = ssh.read()
        print r
        ret = 0

    except pexpect.EOF:
        print 'EOF'
        ssh.close()
        ret = -1
    except pexpect.TIMEOUT:
        print 'TIMEOUT'
        ssh.close()
        ret = -2
    return ret



if __name__ == '__main__':
    ssh_cmd('192.168.56.200','root','toor','df -h')

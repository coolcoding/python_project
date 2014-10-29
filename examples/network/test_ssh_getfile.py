#!/usr/bin/env python

import paramiko
import os


hostname = '192.168.56.2'
username = 'root'
passwd = 'toor'
port = 22
dir_path = '/tmp'


if __name__ == '__main__':
    t = paramiko.Transport(hostname,port)
    t.connect(username=username,password=passwd)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for file in files:
        sftp.get(os.path.join(dir_path,file),file)
    sftp.close()

#!/usr/bin/env python

import subprocess
import time


IP_LIST = ['baidu.com','yahoo.com','sohu.com','qq.com']

cmd_stub = 'ping -c 5 %s'




def do_ping(addr):
    print time.asctime(), 'DONGING PING FOR',addr
    cmd = cmd_stub % addr
    return subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)

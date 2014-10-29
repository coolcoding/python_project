#!/usr/bin/env python
#coding:utf8
import re
import sys
contents = sys.argv[1]
def NginxIpHite(logfile_path):
        #IP：4个字符串，每个1到3个数字，由点连接
        ipadd = r'\.'.join([r'\d{1,3}']*4)
        re_ip = re.compile(ipadd)
        iphitlisting = {}
        for line in open(contents):
                match = re_ip.match(line)
                if match:
                        ip = match.group( )
                        #如果IP存在增加1，否则设置点击率为1
                        iphitlisting[ip] = iphitlisting.get(ip, 0) + 1
        print iphitlisting
NginxIpHite(contents)
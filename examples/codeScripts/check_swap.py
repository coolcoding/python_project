#!/usr/bin/python 
#coding:utf-8 
#列出系统进程占用SWAP的情况！ 
 
import re 
import sys 
import os 
 
def check(pid): 
    #获取SWAP大小 
    file_smaps = '/'.join(["/proc",pid,"smaps"]) 
    f = open(file_smaps,'r') 
    content1 = f.read() 
    f.close()   
    pattern1 = r'Swap:\s+(.*)\s+kB' 
    find1 = re.compile(pattern1) 
    sum = 0 
    for size in  find1.findall(content1): 
        sum = sum + int(size) 
         
    #获取进程名称 
    file_status = '/'.join(["/proc",pid,"status"]) 
    s = open(file_status, 'r') 
    content2 = s.read() 
    s.close() 
    pattern2 = r'Name:\s+(.*)' 
    find2 = re.compile(pattern2) 
    name = find2.findall(content2)[0] 
    return name,sum 
 
if __name__ == "__main__": 
    print "脚本将列出有占用SWAP的程序ID和占用的SWAP大小：" 
    print "%-5s    %-10s    %s" %    ('PID','SWAP(kB)','NAME') 
    print "----------------------------------------------------" 
    for pid in  os.listdir("/proc"): 
        if pid.isdigit(): 
            name,size = check(pid) 
            if size: 
                print "%-5s    %-10s    %s" %    (pid, size, name)

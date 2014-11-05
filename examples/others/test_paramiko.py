#!/usr/bin/python   
#-*- coding: utf-8 -*-  
import paramiko  
import threading  
def ssh2(ip,username,passwd,cmd,port=22):  
    try:  
        ssh = paramiko.SSHClient()  
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
        ssh.connect(ip,port,username,passwd,timeout=5)  
        for m in cmd:  
            stdin, stdout, stderr = ssh.exec_command(m)  
#           stdin.write("Y")   #简单交互，输入 ‘Y’   
            out = stdout.readlines()  
            #屏幕输出  
            for o in out:  
                print o,  
        print '%s\tOK\n' % (ip)  
        ssh.close()  
    except :  
        print '%s\tError\n' % (ip)  
if __name__=='__main__':  
    cmd = ['cal','df -h']#你要执行的命令列表  
    username = "root"  #用户名  
    passwd = "toor"    #密码  
    threads = []   #多线程  
    print "Begin......" 
    ip = '192.168.56.5'
    a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))   
    a.start() 

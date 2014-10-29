#!/usr/bin/env python   
import os 
def load_stat(): 
    loadavg = {} 
    f = open("/proc/loadavg") 
    con = f.read().split() 
    f.close() 
    loadavg['lavg_1']=con[0] 
    loadavg['lavg_5']=con[1] 
    loadavg['lavg_15']=con[2] 
    loadavg['nr']=con[3] 
    loadavg['last_pid']=con[4] 
    return loadavg 
def memory_stat():   
    mem = {}   
    f = open("/proc/meminfo") 
    lines = f.readlines() 
    f.close() 
    for line in lines: 
        if len(line) <2: continue 
    name = line.split(':')[0] 
    var = line.split(':')[1].split()[0] 
    mem[name] =  long(var) /1024 
    mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached'] 
    return mem 
def disk_stat(): 
    import os 
    hd={} 
    disk = os.statvfs("/") 
#    print disk 
    hd['available'] = disk.f_bsize * disk.f_bavail / 1024000 
    hd['capacity'] = disk.f_bsize * disk.f_blocks /1024000 
    hd['used'] = disk.f_bsize * disk.f_bfree /1024000 
    return hd 
#print disk_stat() 
print "mem'used" ,  memory_stat()['Buffers'] 
print "loadavg",load_stat()['lavg_15'] 
print "hd's used",disk_stat()['used'] 
def lsof_stat(): 
    passbin= {} 
    cmd = 'cat /etc/passwd'
    textlist = os.popen(cmd).readlines() 
    for line in textlist: 
#        if len(line) <2: continue 
#        if len(line) <2: continue 
        if line == '\n': 
            name = line.split(':')[0] 
            bin = line.split(':')[6] 
            passbin[name] = bin 
    return passbin 
print lsof_stat()

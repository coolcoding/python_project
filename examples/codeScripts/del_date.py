#!/usr/bin/env python
#-*- coding:UTF-8 -*-
"""
@Item   :  database Backup
@Author :  Kevin Jiang
@Date   :  2013-02-26
@Funtion:
 
    
"""
 
import os,sys,time,re,socket,threading,json,base64,traceback,ConfigParser,fcntl,struct
from rsync_log import rsync_log
from rsync_post import rsync_post
from  statvfs import F_BLOCKS,F_BAVAIL,F_BSIZE
 
pcg = 0
""" 生成斐波那契数列"""
lists = []
a,b = 0,1
while b <= 365:
    a,b = b ,a+b
    lists.append(b)
 
 
class rsync_thread(threading.Thread):
    def __init__(self,path):
        threading.Thread.__init__(self)
        self.log = rsync_log()
        self.path = path
 
 
    """ 计算当前磁盘的使用百分比"""
    def disk(self):
        try:
            vfs = os.statvfs(self.path)
            disk_full = int(vfs[F_BLOCKS]*vfs[F_BSIZE]/1024/1024/1024)
            disk_free = int(vfs[F_BAVAIL]*vfs[F_BSIZE]/1024/1024/1024)
            return  '%.1f'%(float(disk_full - disk_free) / disk_full * 100)
        except:
            self.log.log_info('rsync_info.err','dfile.disk',traceback.print_exc())
            return traceback.print_exc()
 
 
    def run(self):
        global pcg
        old_df = []     # 上一年的删除历史文件
        new_df = []     # 今年的删除历史文件
        sf = []         # 保留的历史文件
        res = {}        # 所有文件的天数及文件的路径
        rs = 0          # 删除文件的总和
        size = []       # 获取删除文件的大小
        msize = []      # 今天备份所有文件的大小
        tday_size = []  # 今天备份文件的大小
        ms = 0          # 今天备份文件的总和
        year = time.localtime().tm_year
 
        """ 得到文件的天数，以文件名作为key，天数作为value """
        for root,dirs,files in os.walk(self.path):
            for fpath in files:
                res[os.path.join(root,fpath)] =  time.localtime(os.stat(os.path.join(root,fpath)).st_ctime).tm_yday
 
        """ 判断文件的天数是否符合斐波那契数列，符合条件append到sf列表中,不符合append df列表中 """
        for v,k in  res.items():
            if k in lists:
                sf.append(k)
                self.log.log_info('log_info.save','dfile.rsync_thread','%s:::%s'%(v,k))
            elif k not in lists:
                if year != time.localtime(os.stat(v).st_ctime).tm_year:
                    old_df.append({v:k})
                else:
                    new_df.append({v:k})
            try:
                for s in  range(len(new_df)):
                    for f,k in new_df[s].items():
                        tday_size.append(k)
                if max({}.fromkeys(tday_size).keys()) == k:
                    msize.append(os.path.getsize(f))
            except:
                pass
        c = []
        pcg = float(self.disk())
        """ 判断今天是否有新的文件备份，在删除的列表中删除最后一天的数据，但必须保证磁盘的使用百分比大于等于 %91 """
        if time.localtime().tm_yday in res.values():
            if len(old_df) != 0:
                for s in  range(len(old_df)):
                    for f,k in old_df[s].items():
                        c.append(k)
                for s in  range(len(old_df)):
                    for f,k in old_df[s].items():
                        if min({}.fromkeys(c).keys()) == k and pcg > 91:
                            size.append(os.path.getsize(f))
                            os.system('rm -frv %s' %f)
                            self.log.log_info('log_info.delete','remove cmd','rm -frv %s %s'%(f,k))
                        elif pcg <= 91:
                            break
                        pcg = float(self.disk())
            elif len(new_df) != 0:
                for s in  range(len(new_df)):
                    for f,k in new_df[s].items():
                        c.append(k)
                for s in  range(len(new_df)):
                    for f,k in new_df[s].items():
                        if min({}.fromkeys(c).keys()) == k and pcg > 91:
                            size.append(os.path.getsize(f))
                            os.system('rm -frv %s' %f)
                            self.log.log_info('log_info.delete','remove cmd','rm -frv %s %s'%(f,k))
                        elif pcg <= 91:
                            break
                        pcg = float(self.disk())
            for s in size:
                rs += s
            for m in msize:
                ms += m
            self.log.log_info('log_info.delete','Disk release %s %s MB'%(self.path,rs /1024/1024) ,'Disk append %s %s MB'%(self.path,ms /1024/1024))
        else:
            self.log.log_info('log_info.delete','Disk files ',' %s No update file' %self.path)
            sys.exit()
 
 
class rsync_dfile(object):
    def __init__(self):
 
    def work(self):
        fp =  open('/proc/mounts','r')
        m_info=fp.readlines()
        fp.close()
        data = {}
        sections = []
 
        for i in m_info:
            if i.find('data=ordered') != -1 or  i.find('mfs') != -1 or i.find('nfs') != -1:
                if os.path.ismount(str(i.split()[1])):
                    if str(i.split()[1]) != '/':
                        if str(i.split()[1]) != '/root':
                            if str(i.split()[1]) != '/var':
                                if len(i.split()[1]) != 1:
                                    if not i.find('sunrpc') != -1:
                                        rs_thread = rsync_thread(i.split()[1])
                                        rs_thread.start()
 
 
if __name__ == "__main__":
    rs = rsync_dfile()
    while True:
        rs.work()
        if pcg <= 91:
             break
#!/usr/bin/env python
#coding:utf-8
import time
import os
data_path = "/data/"
sql_user = "root"
sql_pwd = "root"
sql_ip = "127.0.0.1"
all = "--all-databases"
def mysql_backup():
    backup_name = data_path + time.strftime('%Y%m%d') + '.sql'
    sql_comm = 'mysqldump %s -h%s -u%s -p%s > %s'%(all,sql_ip,sql_user,sql_pwd,backup_name)
    print sql_comm
    if os.system(sql_comm) ==0:
        print"数据库备份成功!"
    else:
        print"数据库备份失败!"
def main():
    SQL_backup = mysql_backup()
    print SQL_backup
if __name__ == "__main__":
    main()

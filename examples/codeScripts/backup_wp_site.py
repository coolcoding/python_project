#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
	wordpress 备份脚本 
        备份网站，添加apache伪静态支持.htaccess,备份数据库
        网站备份位置:/data/backup/wordpress_backup
        #备份全部wordpress网站
        python  backup_wp_site.py
        #备份指定wordpress网站
        python backup_wp_site.py -f filename(每行一网站 www开头)
'''
import os
import shutil
import sys
from string import Template
import re
from  optparse  import OptionParser


wp_conf_path = '/usr/local/nginx/conf/vhosts/wordpress'
backup_site = '/data/backup/wordpress_backup'
wp_path = '/data/wwwroot/wordpress'
dbrootpass = '8pIi5crkPpUbLazs'



with open('htaccess','r') as htf:
    ht_con = htf.read()




def writeHtaccess(path,d=dict()):
    global ht_con
    con = Template(ht_con)    
    con = con.safe_substitute(d)
    with open(path,'w+') as ff:
        ff.write(con)
    
def is_exist(path):
    if os.path.exists(path):
        return path
    else:
        print '%s has not found!' % path
        sys.exit(1)


def getDbInfo(path):
    
    '''from config get db info'''

    if os.path.isfile(path):
        with open(path) as f:
            con = f.read()      
        user_pattern = r'\s+fastcgi_param USERNAME\s+(.*);'
        user_pattern_obj = re.compile(user_pattern)
        dbuser = user_pattern_obj.findall(con)[0]
        db_pattern = r'\s+fastcgi_param DATABASE\s+(.*);'
        db_pattern_obj = re.compile(db_pattern)
        dbname = db_pattern_obj.findall(con)[0]
        pass_pattern = r'\s+fastcgi_param PASSWORD\s+(.*);'
        pass_pattern_obj = re.compile(pass_pattern)
        dbpass = pass_pattern_obj.findall(con)[0]
        return [dbname,dbuser,dbpass]
    return None
        


def backup_one_site(site):

    '''backup one site'''

    if site.startswith('www'):
        site_src = is_exist(os.path.join(wp_path,site + '/webroot'))
        site_dest = os.path.join(backup_site,site)
        if not os.path.isdir(site_dest):
            shutil.copytree(site_src,site_dest)
        ht_site_dest = os.path.join(site_dest,'.htaccess')
        writeHtaccess(ht_site_dest,dict(host=site[4:]))
        conf_src = is_exist(os.path.join(wp_conf_path,site + '.conf'))
        info =  getDbInfo(conf_src)
        if not info:
            print 'database infomation not found'
            sys.exit(1)
        print info
        dump_command  = 'mysqldump -uroot -p%s %s > %s' % (dbrootpass,info[0],os.path.join(site_dest,info[0]+'.sql'))
        os.system(dump_command)
        wp_list = '%s | %s\n' %  (site,' | '.join(info))
        with open('wp_list_info','w+') as wpinfo:
            wpinfo.write(wp_list)
 

    
def backup_all():

    '''backup all wordpress site'''

    for site in os.listdir(wp_path):
        backup_one_site(site)
        sys.exit(1)


def walk_backup_site(infile):

    '''backup site in file infile'''

    if not os.path.isfile(infile):
        print 'file %s not found!' % infile
        sys.exit(1)

    for site in file(infile):
        site = site.strip()
        backup_one_site(site)


if __name__ == '__main__':
    print __doc__
    usage = "usage: %prog [option]"
    parse = OptionParser(usage=usage)
    parse.add_option('-f','--file',dest='filename',default='all',help='read data from filename')
    parse.add_option('-p','--password',dest='passwd',help='mysql root password')
    (opt,args) = parse.parse_args()
    if opt.passwd:
        dbrootpass = opt.passwd
    if not opt.filename == 'all':
        walk_backup_site(opt.filename)
    else:
        backup_all()

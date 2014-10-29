#!/usr/bin/env python
#coding:utf-8

'''抓取centoscn.com网站下python下的文章列表'''

import urllib
import os
import re

wwwroot="/data/wwwroot/www.centoscn.com"
pylist=[]
for i in range(1,5):
    links = "http://www.centoscn.com/python/list_20_%s.html" % i
    urls = urllib.urlopen(links)
    con = urls.read()
    id_list = con.find(r'id="list"')
    id_list_div = con.find(r'</div>',id_list)
    li_start = con.find('li',id_list)
    href = con.find('href=',li_start)
    html = con.find('html',href)
    pagelist=[con[href+6:html+4]]
    while href != -1 and html != -1:
        href = con.find('href=',html)
        html = con.find('html',href,id_list_div)
        con_li = con[href+6:html+4]
        if con_li:
            pagelist.append(con_li)

    pylist.append(pagelist)


j=1
for pls in  pylist:
    list_dir = wwwroot +  "/python/list_20_%s" % j
    j+=1
    if not os.path.isdir(list_dir):
        os.makedirs(list_dir)
    for pl in pls:
        tmp = "http://www.centoscn.com%s" %  pl
        file_tmp = re.sub(r'.*/','',tmp)
        file_path = list_dir + '/' + file_tmp
        url_tmp = urllib.urlopen(tmp)
        con_tmp = url_tmp.read()
        f = open(file_path,'w+')
        f.write(con_tmp)
        f.flush()
        f.close()

#!/usr/bin/env python
#coding:utf-8


'''
   抓取卢松松整个博客的所有文章 
   链接地址http://lusongsong.com
'''

import time
import urllib
import os

alllist = []
for i in range(1,73):
    urllist = [] 
    h2_begin = h2_end = href = html = 0
    urlinks = 'http://lusongsong.com/default_%s.html' % i
    uls = urllib.urlopen(urlinks)
    con = uls.read()
    h2_begin = con.find(r'<h2>')
    h2_end = con.find(r'</h2>')
    href = con.find(r'href=',h2_begin)
    html = con.find(r'.html',href,h2_end)
    cc = con[href+6:html+5]
    urllist.append(cc)
    while h2_begin != -1 and h2_end != -1 and href != -1 and html != -1:
        h2_begin = con.find(r'<h2>',h2_end)
        h2_end = con.find(r'</h2>',h2_begin)
        href = con.find(r'href=',h2_begin)
        html = con.find(r'.html',href,h2_end)
        cc = con[href+6:html+5]
        if cc != '':
            urllist.append(cc)
    alllist.append(urllist)

print len(alllist)

j = 1 
for urllist in alllist:
    default_dir = "/data/wwwroot/www.lss.com/webroot/default_%s" % j
    os.makedirs(default_dir)
    for url in urllist:
        name = url[27:]
        ul = urllib.urlopen(url)
        f = open(default_dir + '/' + name,'w+')
        f.write(ul.read())
        f.close()
        time.sleep(10)
    j+=1

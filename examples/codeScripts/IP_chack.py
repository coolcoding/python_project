#!/usr/bin/python
import sys
import urllib2
import re
IP = raw_input("address ip:")
def check(IP):
   url = urllib2.urlopen('http://www.ip138.com/ips1388.asp?ip={0}&action=2'.format(IP))
#   url = urllib2.urlopen('http://www.ip138.com/ips1388.asp?ip=%s&action=2' % IP )
   result = url.read()
   re_result = re.compile('<ul class="ul1"><li>(.*?)</li><li>(.*?)</li></ul>')
   data = re_result.findall(result)[0]
   print data[0]
   print data[1]
check(IP)
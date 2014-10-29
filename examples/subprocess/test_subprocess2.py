#!/usr/bin/env python

import subprocess

p = subprocess.Popen('tr a-z  A-Z',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
output,error = p.communicate('hello world')
print output

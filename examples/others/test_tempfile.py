#!/usr/bin/env python
#coding:utf-8

import tempfile,os
temp = tempfile.mktemp()
open(temp,'w')
os.close(file)
os.remove(file)

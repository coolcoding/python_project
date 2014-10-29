#!/usr/bin/env python
from optparse import OptionParser

usage = "usage: %prog [option] arg1 arg2"
parse = OptionParser(usage=usage)
parse.add_option('-f','--file',dest="filename",help="read data from FILENAME")
(opt,args) = parse.parse_args()
if len(args) < 1:
    parse.error('incorrect number of args')
if opt.filename:
    print opt.filename
print opt
print args

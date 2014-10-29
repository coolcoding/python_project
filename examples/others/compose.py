#!/usr/bin/env python
#coding:utf-8


'''\033[;31m
    lambda 对于需要一个函数作为变元的函数(map,filter,reduce) 有用
    Usage: python scriptname var
    \033[0m
'''


import sys

def compose(func1,func2,y):
    f = lambda x,f1 = func1,f2 = func2:f1(f2(y))
    return f(y)

if len(sys.argv) > 1:
    var = int(sys.argv[1])
    print compose(chr,abs,var)
else:
    print __doc__
    print sys.modules
    print sys.path

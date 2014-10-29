#!/usr/bin/env python 

from multiprocessing import Process,Queue
import os,time,random


def  write(q):
    for v in ['A','B','C']:
        print 'Put %s to queue...' % v
        q.put(v)
        time.sleep(random.random())

#!/usr/bin/env python

from  multiprocessing   import Process
import os


def run_proc(name):
    print 'Run child process %s(%s)'  % (name,os.getpid())


if __name__ == '__main__':
    print 'parent process %s.' %  os.getpid()
    p = Process(target=run_proc,args=('test',))
    print 'Process start..'
    p.start()
    p.join()
    print 'Process end..'

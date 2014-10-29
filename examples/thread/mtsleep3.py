#!/usr/bin/env python

from time import ctime,sleep
import threading

loops = [2,4]
class  ThreadFunc():
    def __init__(self,func,args,name=''):
        self.name = name
        self.func = func
        self.args = args
    def __call__(self):
        apply(self.func,self.args)
def loop(nloop,nsec):
    print 'start loop',nloop,'at',ctime()
    sleep(nsec)
    print 'loop',nloop,'done at:',ctime()

def main():
    print 'starting at:',ctime()
    nloops = range(len(loops))
    threads = []
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop,(i,loops[i])))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print 'all Done at:',ctime()

if __name__ == '__main__':
    main()

#!/usr/bin/env python

from multiprocessing import Pool

import os,time,random



def run_time_task(name):
    print 'Run task %s(%s)..(%s)' % (name,os.getpid(),time.strftime('%Y%m%d %H:%M:%S'))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print 'Task %s runs %0.2f s (%s)' % (name,end - start,time.strftime('%Y%m%d %H:%M:%S'))



if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool(3)
    for i in range(5):
        p.apply_async(run_time_task,args = (i,))
    print 'waiteing for all subprocess done...'
    p.close()
    p.join()
    print 'All subprocess done'

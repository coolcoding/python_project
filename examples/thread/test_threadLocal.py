#!/usr/bin/env python

import threading


local_school = threading.local()

def process_student():
    print 'Hello,%s (in %s)\n' % (local_school.student,threading.currentThread().name)



def process_thread(name):
    local_school.student = name
    process_student()



t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()

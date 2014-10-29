#!/usr/bin/env python
import threading
import time

count = 1

class KillThread(threading.Thread):
    def run(self):
        global count
        print 'thread # %s:Pretending to do stuff' % count
        count += 1
        time.sleep(2)
        print 'done with stuff'

for t in range(5):
    KillThread().start()

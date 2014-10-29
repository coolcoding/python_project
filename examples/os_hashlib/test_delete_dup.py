#!/usr/bin/env python
from  test_checksum_diskwalk import findDups
import os

def delete(path):
    dup = findDups(path)
    for d in dup:
        print 'deleting %s' % d
        os.remove(d)

if __name__=='__main__':
    delete('/root/python')

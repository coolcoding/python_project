#!/usr/bin/env python
from  checksum  import create_checksum
from diskwalk import diskwalk 
import os

def findDups(path):
    d = diskwalk(path)
    files = d.enumeratePaths()
    dup = []
    record = {}
    for file in files:
        compound_key = (os.path.getsize(file),create_checksum(file))
        print compound_key
        if compound_key in record:
            dup.append(file)
        else:
            record[compound_key] = file
    return dup


if __name__ == '__main__':
    print  '%proxy'
    for d in findDups('/root/python'):
        print d

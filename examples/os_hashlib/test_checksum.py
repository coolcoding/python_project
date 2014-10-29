#!/usr/bin/env python
from checksum import create_checksum 

if create_checksum('file1') == create_checksum('file2'):
    print 'same'
else:
    print 'diff'

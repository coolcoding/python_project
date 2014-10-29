#!/usr/bin/env python

import hashlib

md5 = hashlib.md5()

md5.update('0123456')

print md5.hexdigest()

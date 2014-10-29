#!/usr/bin/env python

import os,sys
import pexpect

log = pexpect.run('ls /root')
print log

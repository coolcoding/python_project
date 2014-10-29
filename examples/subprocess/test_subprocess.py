#!/usr/bin/env python

import subprocess



def nulti(*args):
    for cmd in args:
        p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        out = p.stdout.read()
        print out




if __name__ == '__main__':
    nulti('df -h','ls $(pwd)')

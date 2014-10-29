#!/usr/bin/env python

class Chain(object):
    def __init__(self,path = ''):
        self.path = path


    def __getattr__(self,path):
        return Chain('%s/%s' % (self.path,path))
        

    def __str__(self):
        return self.path


print Chain().user.name.aaa

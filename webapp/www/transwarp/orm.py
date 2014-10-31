#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'coolcoding'

import time,logging

class Model(dict):


    def __init__(self,**kw):

        super(Model,self).__init__(**kw)
        

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)


    def __setattr__(self,key,value):
        
        self[key] = value



if __name__ == '__main__':
    m = Model()
    print m.user

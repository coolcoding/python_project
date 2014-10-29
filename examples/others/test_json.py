#!/usr/bin/env python
#!coding:utf-8
'''json格式输出序列化'''
import json


d = dict(name = 'mike',age = 33,score = 88)


print json.dumps(d)



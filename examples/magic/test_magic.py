#!/usr/bin/env python

class Student(object):
    def __init__(self,num = 1):
        self.num = num

    def __repr__(self):
        return 'repr'


    def __str__(self):
        return  'str'

    def __iter__(self):
        return self

    def next(self):
        self.num += 1
        if self.num > 100:
            raise StopIteration()
        return self.num

    def __getattr__(self,attr):
        l = len(attr)
        if attr[l-2:] == '()':
            return 25
        else:
            return 99

    def __call__(self):
        print 'call'





s = Student()
print s.score
print callable(s)
print s()

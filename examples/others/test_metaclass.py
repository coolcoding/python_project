#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
__new__()方法接收到的参数依次是：
当前准备创建的类的对象；
类的名字；
类继承的父类集合；
类的方法集合。


'''

class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)



class MyList(list):
    __metaclass__ = ListMetaclass


L = MyList()
L.add(2)
print L

#!/usr/bin/python
#!coding:utf-8
import functools
'''函数'''



#匿名函数
print  map(lambda x: x * x,[1,2,3,4,5])

#匿名函数转换成一般函数
def Test(x):
    return x * x

print [Test(x) for x in range(3)]


#不带参数装饰器(decorator)
print '不带参数装饰器'
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print 'call %s()' % func.__name__
        return func(*args,**kw)
    return wrapper

@log
def now():
    print 'now is today'

print now.__name__
now()

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s()' % (text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

@log2('hello')
def now2():
    print 'now2 today'

now2()


print '偏函数'
print int('22',base=16)

int2 = functools.partial(int,base=2)
print int2('100000')

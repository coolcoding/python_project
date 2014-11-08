#!/usr/bin/env python



print map(lambda x: x*x,[1,2,3,4,5,6])





def add(x,y):
    return x + y

def fn(x,y):
    return x * 10 + y
print reduce(add,[1,2,3,4,5])
print reduce(fn,[1,2,3,4,5])


#str to int
def str2int(s):
    def fn(x,y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]   
#    return reduce(fn,map(char2num,s))
    return reduce(lambda x,y: x*10+y,map(char2num,s))

print type(str2int('12345'))

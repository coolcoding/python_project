#!/usr/bin/env python


from collections import namedtuple

Point = namedtuple('Point',['x','y'])
p = Point(1,2)


print p.x,p.y


Circle = namedtuple('Circle',['x','y','r'])

c = Circle(6,6,9)

print c.x,c.r

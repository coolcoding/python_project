#!/usr/bin/env python


from collections import deque


q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print q

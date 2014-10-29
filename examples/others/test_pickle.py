#!/usr/bin/env python
'''序列化'''

try:
    import cPickle as pickle
except:
    import pickle



d = dict(name = 'bob',age = '22',score = '99')

#print pickle.dumps(d)



with open('dump.txt','wb') as f:
    pickle.dump(d,f)


with open('dump.txt','rb') as f:
    dd = pickle.load(f)

print dd

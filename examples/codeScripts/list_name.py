import os
import os.path
rootdir='./test/'
out=open('names.txt','w')
for parent,dirnames,filenames in os.walk(rootdir):
    print "**********"
    for name in filenames:
        if '.txt'==name[-4:]:
            out.write(name[:-4]+'\n')
        elif '.jpg'==name[-4:]:
            out.write(name[:-4]+'\n')
        elif '.rm'==name[-3:]:
            out.write(name[:-3]+'\n')
        else:
            continue
    for dirname in dirnames:
        out.write('*********\n')
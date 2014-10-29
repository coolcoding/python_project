#!/usr/bin/env python
from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy.orm  import mapper,sessionmaker
import os


path = '/tmp'


#part 1:create engine

engine = create_engine('sqlite:///:memory:',echo=False)

#Part 2: metadata

metadata = MetaData()


filesystem_table = Table('filesystem',metadata,
    Column('id',Integer,primary_key=True) ,
    Column('path',String(500)),
    Column('file',String(255)),
    )

metadata.create_all(engine)

#Part 3:mapped class


class FileSystem(object):
    def __init__(self,path,file):
        self.path = path
        self.file = file
    def __repr__(self):
        return "[FileSystem('%s','%s')]" % (self.path,self.file)


#Part 4:mapper  function

mapper(FileSystem,filesystem_table)

#Part 5:create sesstion

Session = sessionmaker(bind=engine,autoflush=True)
sesstion = Session()

#Part 6:crawl file system and populate databse with results
for dirpath,dirnames,filenames in os.walk(path):
    for file in filenames:
        fullpath = os.path.join(dirpath,file)
        record = FileSystem(fullpath,file)


#Part 7:commit to the database

sesstion.commit()


#Part 8:query
for record in sesstion.query(FileSystem):
    print "database record Number:%s,File:%s " % (record.id,record.path,record.file)

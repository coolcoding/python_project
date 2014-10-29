#!/usr/bin/env python
#coding:utf-8
'''sqllite的数据库'''
import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#print cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#print cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
#print cursor.rowcount
cursor.execute('select * from user where id = ?','1')
print cursor.fetchall()
cursor.close()
conn.commit()
conn.close()


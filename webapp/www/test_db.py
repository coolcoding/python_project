#!/usr/bin/env python


from models import User,Blog,Comment

from transwarp import db


db.create_engine(user='root',password='root',database='awesome')
u = User(name='Test',email='1029@qq.com',password='13413512',image='about:blank')


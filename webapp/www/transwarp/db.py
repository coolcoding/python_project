#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'coolcoding'

import time, uuid, functools, threading, logging

class Dict(dict):


    def __init__(self,names=(),values=(),**kw):
        super(Dict,self).__init__()
        for k,v in zip(names,values):
            self[k] = v

    def __getattr__(self,k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError('Dict object has not attribute %s' % k)

    def __setattr__(self,k,v):
        self[k] = v


# global engine object:
engine = None

class _Engine(object):
    def __init__(self,connect):
        self._connect = connect

    def connect(self):
        return self._connect()



def create_engine(user,password,database,host='127.0.0.1',port=3306,**kw):
    import mysql.connector
    global engine
    if engine is not None:
        raise DBError('Engine is already initialized.')
    params = dict(user=user,password=password,database=database,host=host,port=port)
    defaults = dict(use_unicode=True, charset='utf8', collation='utf8_general_ci', autocommit=False)
    for k, v in defaults.iteritems():
        params[k] = kw.pop(k, v)
    params.update(kw)
    params['buffered'] = True
    engine = _Engine(lambda: mysql.connector.connect(**params))
    logging.info('Init mysql engine <%s> ok.' % hex(id(engine)))


class _LasyConnection(object):

    def __init__(self):
        self.connection = None

    def cursor(self):
        if self.connection is None:
            connection = engine.connect()
            logging.info('open connection <%s>...' % hex(id(connection)))
            self.connection = connection
        return self.connection.cursor()
    
    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def cleanup(self):
        if self.connection:
            connection = self.connection
            self.connection = None
            logging.info('close connection <%s>' % hex(id(connection)))
            connection.close()

        
class _DbCtx(threading.local):
        
    def __init__(self):
        self.connection = None

    def isInit(self):
        return not self.connection is None

    def init(self):
        logging.info('open lasy connection...')
        self.connection = _LasyConnection()
        self.connection.cursor()

    def cleanup(self):
        self.connection.cleanup()
        self.connection = None

    def cursor(self):
        return self.connection.cursor()


#thread-local db context
_db_ctx = _DbCtx()


class _ConnectionCtx(object):
    def __enter__(self):
        global _db_ctx
        self.should_cleanup = False
        if not _db_ctx.isInit():
            _db_ctx.init()
            self.should_cleanup = True
        return self

    def __exit__(self, exctype, excvalue, traceback):
        global _db_ctx
        if self.should_cleanup:
            _db_ctx.cleanup()
        

def with_connection(func):
    '''
    Decorator for reuse connection
    '''
    @functools.wraps(func)
    def _wrapper(*args,**kw):
        with _ConnectionCtx():
            return func(*args,**kw)
    return _wrapper

@with_connection
def _update(sql,*args):
    global _db_ctx
    cursor = None
    sql = sql.replace('?','%s')
    logging.info('SQL: %s, ARGS: %s' % (sql,args))
    try:
        cursor = _db_ctx.connection.cursor()
        cursor.execute(sql,args)
        _db_ctx.connection.commit()
        r = cursor.rowcount
        return r
    finally:
        if cursor:
            cursor.close()

def insert(table,**kw):
    cols, args = zip(*kw.iteritems())
    sql = 'insert into `%s` (%s) values (%s)' % (table,','.join(['`%s`' % col for col in cols]),','.join(['?' for i in range(len(cols))]))
    print sql
    return _update(sql,*args)


def update(sql,*args):
    return _update(sql,*args)
    

def delete(table,**kw):
    cols, args = zip(*kw.iteritems()) 
    where = 'and'.join(['`%s`= %s' % (i,'?') for i,j in zip(cols,args)])
    sql = 'delete from `%s` where %s' % (table,where)
    return _update(sql,*args)



def _select(sql,first,*args):

    global _db_ctx
    cursor = None
    sql = sql.replace('?','%s')
    logging.info('SQL:%s ,ARGS: %s' % (sql,args))
    try:
        cursor = _db_ctx.connection.cursor()
        cursor.execute(sql,args)
        names =[x[0] for x in cursor.description] 
        if first:
            values = cursor.fetchone()
            if not values:
                return None
            return Dict(names,values)
        return [Dict(names,x) for x in cursor.fetchall()]
    finally:
        if cursor:
            cursor.close()

    
@with_connection
def select_one(sql,*args):
    '''
    select_one('select * from user where id = ?','1')
    '''
    return _select(sql,True,*args)


@with_connection    
def select_int(sql,*args):
    
    d = _select(sql,True,*args)
    if len(d) != 1:
        raise MuiltiColumnsError('Expect only one column.')
    return d.values()[0]


@with_connection
def select(sql,*args):
    '''
    select('select * from user where id = ?','1')
    '''
    return _select(sql,False,*args)

def next_id(t=None):
    '''
    Return next id as 50-char string.

    Args:
        t: unix timestamp, default to None and using time.time().
    '''
    if t is None:
        t = time.time()
    return '%015d%s000' % (int(t * 1000), uuid.uuid4().hex)


def _profiling(start, sql=''):
    t = time.time() - start
    if t > 0.1:
        logging.warning('[PROFILING] [DB] %s: %s' % (t, sql))
    else:
        logging.info('[PROFILING] [DB] %s: %s' % (t, sql))




if __name__ == '__main__':
    logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(filename)s [line:%(lineno)d] method:(%(funcName)s) message:{%(message)s}'
            )
    create_engine('root','root','test')
#    print insert('user',id='2',name='lo')
#    print update('update user set name = ? where id = ?','good','1')
#    print delete('user',id='1')
    print select_one('select * from user where id = ?','1')
    print select('select * from user where id = ?','1')

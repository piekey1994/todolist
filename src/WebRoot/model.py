# -*- coding: utf-8 -*-v
import MySQLdb
from flask import g

def getJoke():
    cur=g.db.cursor()
    sql="select text from joke order by rand() limit 1"
    cur.execute(sql)
    result=cur.fetchall()
    return result[0][0]

def isExsit(name):
    sql="select * from user where name='%s'" %(name)
    g.cur.execute(sql)
    result=cur.fetchall()
    if(len(result)==0):
        return False
    else:
        return True
    
def addUser(name,password):
    sql="insert into user(name,password) values('%s',password('%s'))" %(name,name+password)
    g.cur.execute(sql)
    
def isTure(name,password):
    sql="select * from user where name='%s' and password=password('%s')" %(name,name+password)
    g.cur.execute(sql)
    result=g.cur.fetchall()
    if(len(result)==0):
        return False
    else:
        return True
    
def addText(name,text):
    sql="insert into plan(name,text) values('%s','%s')" %(name,text)
    g.cur.execute(sql)

def isYourText(name,num):
    sql="select name from plan where name='%s' and num='%s'" %(name,num)
    g.cur.execute(sql)
    result=g.cur.fetchall()
    if(len(result)==0):
        return False
    else:
        return True
    
def moveText(num):
    sql="update plan set state=2 where num='%s'" %(num)
    g.cur.execute(sql)
    
def deleteText(num):
    sql="update plan set state=0 where num='%s'" %(num)
    g.cur.execute(sql)
    
def getTobedoList(name):
    sql="select num,text from plan where name='%s' and state=1" %(name)
    g.cur.execute(sql)
    return g.cur.fetchall()

def getDoingList(name):
    sql="select num,text from plan where name='%s' and state=2" %(name)
    g.cur.execute(sql)
    return g.cur.fetchall()
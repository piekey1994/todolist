# -*- coding: utf-8 -*-v

from flask import Blueprint
from flask import request
from flask import session

from model import * 
from lib import *
from lib import FormValue
    
userController = Blueprint('userController',__name__)

def isOk(name):
    if len(name)>50:
        return -1
    else:
        spSign=['<','>',' ','\n','&',';']
        for x in spSign:
            if(name.find(x)!=-1):
                return -2
    return 1

@userController.route('/post/login',methods=['POST'])
def login():
    myFormValue=FormValue(request,'name','password')
    if myFormValue.isNone():
        return "你是坏人"
    name,password=myFormValue.getKeyValue()
    if(isTure(name,password)):
        session['name']=name
        return 'true'
    else:
        return createAlert('danger','用户名或密码错误T_T')

@userController.route('/post/register',methods=['POST'])
def register():
    myFormValue=FormValue(request,'name','password')
    if myFormValue.isNone():
        return "你是坏人"
    name,password=myFormValue.getKeyValue()
    if isOk(name)==-1:
        return createAlert('warning','你太长了')
    elif isOk(name)==-2:
        return createAlert('warning','让你别乱写的...')
    elif isExsit(name):
        return createAlert('warning','你的名字太大众了')
    else:
        addUser(name,password)
        return createAlert('success','注册成功啦^_^')
    
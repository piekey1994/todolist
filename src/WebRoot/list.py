# -*- coding: utf-8 -*-v

from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import render_template

from model import * 
from lib import * 
from lib import FormValue
    
listController = Blueprint('listController',__name__)

def isOk(text):
    if len(text)>255:
        return False
    else:
        return True

@listController.route('/post/protected/add',methods=['POST'])
def add():
    name=session.get('name')
    myFormValue=FormValue(request,'text')
    if myFormValue.isNone():
        return "你是坏人"
    text=myFormValue.getKeyValue()
    if(isOk(text)):
        text=changeToHtml(text)
        addText(name, text)
        return 'true'
    else:
        return createAlert('warning','你太长了')

@listController.route('/post/protected/move',methods=['POST'])
def move():
    name=session.get('name')
    numlist=request.form.getlist('numlist')
    if numlist is None:
        return "你是坏人"
    for x in numlist:
        if isYourText(name, x):
            moveText(x)
    return ''

@listController.route('/post/protected/delete',methods=['POST'])
def delete():
    name=session.get('name')
    numlist=request.form.getlist('numlist')
    if numlist is None or numlist==[]:
        return "你是坏人"
    for x in numlist:
        if isYourText(name, x):
            deleteText(x)
    return ''

@listController.route('/protected/showTobedoList')
def showTobedoList():
    name=session.get('name')
    return render_template('tobedoList.html',list=getTobedoList(name))

@listController.route('/protected/showDoingList')
def showDoingList():
    name=session.get('name')
    return render_template('doingList.html',list=getDoingList(name))
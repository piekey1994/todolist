# -*- coding: utf-8 -*-v
from flask import request

class FormValue(object):
    def __init__(self,request,*key):
        self.keyValue=[]
        for x in key:
            self.keyValue.append(request.form[x])
    def isNone(self):
        for x in self.keyValue:
            if x is None or x=='':
                return True
        return False
    def getKeyValue(self):
        return self.keyValue   

def changeToHtml(text):
    newText=[]
    text=list(text)
    for x in text:
        if x==' ':
            newText.append('&nbsp;')
        elif x=='<':
            newText.append('&lt;')
        elif x=='>':
            newText.append('&gt;')
        elif x=='\n':
            newText.append('<br>')
        elif x=='&':
            newText.append('&amp;')
        else:
            newText.append(x)
    return ''.join(newText)

def createAlert(type,text):
    return '''<div class="alert alert-dismissable alert-%s">
            <button type="button" class="close" data-dismiss="alert">×</button>
            <p>%s</p>
            </div>''' %(type,text)
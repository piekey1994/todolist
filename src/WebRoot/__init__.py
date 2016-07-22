# -*- coding: utf-8 -*-v

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import session
from flask import url_for
from flask import g
from model import *
from user import userController
from list import listController

app=Flask(__name__)
app.config['SECRET_KEY'] = 'sdbdth54y&SAH(@PN#*C$!$*QUWDJQ'
app.register_blueprint(userController)
app.register_blueprint(listController)

#过滤器
@app.before_request
def before_request():
    g.db = MySQLdb.connect("localhost","root","112119110","todolist",charset="utf8")
    g.db.autocommit(1)
    g.cur=g.db.cursor()
    reqUrl=request.url
    i=3
    while i>0:
        reqUrl=reqUrl[reqUrl.find('/')+1:]
        i=i-1
    if reqUrl.find('/')!=-1:
        Sroot=reqUrl[:reqUrl.find('/')]
        if Sroot=='post':
            if request.method=='GET':
                return redirect(url_for('index'))
            else:
                reqUrl=reqUrl[reqUrl.find('/')+1:]
                if reqUrl.find('/')!=-1:
                    Sroot=reqUrl[:reqUrl.find('/')]
        if Sroot=='protected':
            userName=session.get('name')
            if userName is None:
                return redirect(url_for('index'))
            
@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'): g.db.close()

@app.route('/')
def index():
    userName=session.get('name')
    if userName is None:
        return render_template('login.html')
    else:
        if session.get('joke') is None:
            session['joke']=getJoke()
        return render_template('index.html', joke=session.get('joke'))
    
@app.route('/exit')
def exit():
    session['name']=None
    session['joke']=None
    return redirect(url_for('index'))
        

if __name__=='__main__':
    app.run(port=8023, debug=True)

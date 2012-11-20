#!/usr/bin/python
#Filename:web.py

from bottle import route,run,template,static_file
import sqlite3

#@route('/')
def index():
    d = sqlite3.connect('test.db')
    db = d.cursor()
    db.execute('SELECT UUID,HEIGHT FROM IMAGE')
    path_list = db.fetchall()
    db.close()
    output = template('model',path_list=path_list)
    return output

@route('/')
@route('/:page#\d+#')
def page(page=1):
    d = sqlite3.connect('test.db')
    db = d.cursor()
    p = int(page)
    page = int(page)*30+1
    db.execute('SELECT UUID,HEIGHT FROM IMAGE WHERE ID BETWEEN %d AND %d'%(page-30,page-1))
    path_list = db.fetchall()
    #db.execute('SELECT COUNT(*) FROM IMAGE')
    #list2 = db.fetchall()
    #p = list2[0][0]
    #p = p/20
    #p = p + 1
    db.close()
    if p == 1:
        output = template('model',path_list=path_list,p = p)
    else:
        output = template('model1',path_list=path_list,p=p)
    return output

@route('/static/:filename')
def server_static(filename):
    return static_file(filename,root='static/')

@route('/image/:filename')
def server_image(filename):
    return static_file(filename,root='image/')

run()

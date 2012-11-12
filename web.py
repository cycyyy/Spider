#!/usr/bin/python
#Filename:web.py

from bottle import route,run,template,debug,static_file
import sqlite3

@route('/')
def index():
    d = sqlite3.connect('test.db')
    db = d.cursor()
    db.execute('SELECT UUID,HEIGHT FROM IMAGE')
    path_list = db.fetchall()
    db.close()
    output = template('model',path_list=path_list)
    return output

@route('/static/:filename')
def server_static(filename):
    return static_file(filename,root='static/')

@route('/image/:filename')
def server_image(filename):
    return static_file(filename,root='image/')

debug(True)
run()

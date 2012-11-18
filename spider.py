#!/usr/bin/python
#Filename:spider.py
import sys
import requests
import re
import sqlite3
import uuid
import urllib
import threading,Queue
import pic
#import makegif

global mutex
mutex = threading.Lock()
class Spider:


    def __init__(self,ad):
        self.ad = ad
        d = sqlite3.connect('test.db')
        db = d.cursor()
        search = 'SELECT PATH FROM IMAGE WHERE LAST=1 AND PAGE=\''+ad+'\''
        db.execute(search)
        self.last = db.fetchone()
        d.close()
        self.queue = Queue.Queue()
        for i in range(10):
            Download(self.queue,i)
        self.crawl()

    def crawl(self):
        url = 'http://zhan.renren.com/'+self.ad+'?from=pages'
        #url = 'http://zhan.renren.com/woaigif?from=pages'
        #url = 'http://zhan.renren.com/yaoxiaomen?from=pages'
        #url = 'http://zhan.renren.com/wenzinvliumang?from=pages'
        #url = 'http://zhan.renren.com/diaosi365?from=pages'
        self.page = 0
        while True:
            try:
                payload = {'page':self.page}
                r = requests.get(url,params = payload)
                result = self.catch(r.content)
                if self.receive(result):
                    for i in range(10):
                        self.queue.put(None)
                    break
                self.page = self.page + 1
                print self.page
            except Exception:
                break;

    def catch(self,html):
        #str1 = r'\);"><img src="'
        str2 = r'data-src="'
        str3 = r'"  />'
        str4 = r'" alt'
        _str = r'(.*)'
        str5 = r'" />'
        str6 = r'<img src="'
        result = re.findall(str6+_str+str4,html)
        #result = re.findall(str5+_str+str4,html)
        result = result + re.findall(str2+_str+str3,html)
        result = result + re.findall(str2+_str+str5,html)
        return result

    def receive(self,result):
        if len(result)==0:
            return True
        for rel in result:
            if self.last!=None and rel == self.last[0]:
                return True
            else:
                if len(rel)<120:
                    name = str(uuid.uuid1())
                    url = rel.split('.')
                    name = name + '.' + url[-1]
                    work = (rel,name)
                    print name
                    self.queue.put(work)
                    mutex.acquire()
                    d = sqlite3.connect('test.db')
                    db = d.cursor()
                    if rel==result[0] and self.page == 0:
                        db.execute('INSERT INTO IMAGE VALUES(NULL,\''+name+'\',\''+rel+'\',\''+self.ad+'\',1,0)')
                        d.commit()
                        if self.last!=None:
                            db.execute('UPDATE IMAGE SET LAST=0 WHERE PATH=\''+self.last[0]+'\'')
                            d.commit()
                    else:
                        db.execute('INSERT INTO IMAGE VALUES(NULL,\''+name+'\',\''+rel+'\',\''+self.ad+'\',0,0)')
                        d.commit()
                    d.close()
                    mutex.release()


class Download(threading.Thread):


    def __init__(self,Myqueue,threadname):
        threading.Thread.__init__(self,name=threadname)
        self.queue = Myqueue
        self.start()

    def run(self):
        while True:
            work = self.queue.get()
            if work == None:
                break
            url = work[0]
            name = work[1]
            urllib.urlretrieve(url,'image/'+name)
            #nlist = name.split('.')
            #if not nlist[-1] == 'gif':
            pt = pic.Pic('image/'+name)
            height = pt.resize()
            mutex.acquire()
            d = sqlite3.connect('test.db')
            db = d.cursor()
            db.execute('UPDATE IMAGE SET HEIGHT='+str(height)+' WHERE uuid=\''+name+'\'')
            d.commit()
            d.close()
            mutex.release()
            #else:
            #    makegif.main('image/'+name)


def main():
    Spider(sys.argv[1])

if __name__=='__main__':main()

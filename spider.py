#!/usr/bin/python
#Filename:spider.py
import requests
import re
import sqlite3
import uuid
import urllib
import threading,Queue
import time

class Spider:


    def __init__(self,ad):
        self.ad = ad
        self.d = sqlite3.connect('test.db')
        self.db = self.d.cursor()
        search = 'SELECT PATH FROM IMAGE WHERE LAST=1 AND PAGE=\''+ad+'\''
        self.db.execute(search)
        self.last = self.db.fetchone()
        self.queue = Queue.Queue()
        for i in range(10):
            Down_image(self.queue,i)
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
                    if rel==result[0] and self.page == 0:
                        self.db.execute('INSERT INTO IMAGE VALUES(\''+name+'\',\''+rel+'\',\''+self.ad+'\',1)')
                        self.d.commit()
                        if self.last!=None:
                            self.db.execute('UPDATE IMAGE SET LAST=0 WHERE PATH=\''+self.last[0]+'\'')
                            self.d.commit()
                    else:
                        self.db.execute('INSERT INTO IMAGE VALUES(\''+name+'\',\''+rel+'\',\''+self.ad+'\',0)')
                        self.d.commit()


class Down_image(threading.Thread):


    def __init__(self,Myqueue,threadname):
        threading.Thread.__init__(self,name=threadname)
        self.queue = Myqueue
        self.start()

    def run(self):
        while True:
            if(self.queue.empty()==False):
                work = self.queue.get()
                url = work[0]
                name = work[1]
                urllib.urlretrieve(url,'image/'+name)
            else:
                time.sleep(1)
                if(self.queue.empty()==True):
                    break


def main():
    a = Spider('diaosi365')

if __name__=='__main__':main()

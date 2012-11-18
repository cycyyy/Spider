#!/usr/bin/python
#Filename:pic.py

from PIL import Image
#import makegif

class Pic(object):


    def __init__(self,path):
        self.path = path
        self.im = Image.open(path)

    def _resize(self,im):
        width = 200
        ratio = float(width)/im.size[0]
        height = int(im.size[1]*ratio)
        re = im.resize((width,height))
        #re.save(self.path)
        return re

    #def gif_resize(self):
    #    image_ = []
    #    self.im.seek(0)
    #    try:
    #        while 1:
    #            image_.append(self._resize(self.im))
    #            self.im.seek(self.im.tell()+1)
    #    except EOFError:
    #        pass
    #    makegif.writeGif(self.path,image_)

    def resize(self):
        re = self._resize(self.im)
        re.save(self.path)
        return re.size[1]

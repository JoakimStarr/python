#!/usr/bin/env python
# coding=utf-8

from PIL import Image,ImageDraw,ImageFont

def addNumTolmg(img,num="99+"):
    images = Image.open(img)
    size = images.size
    # print(size)
    fontsize = size[1]//4
    # print(fontsize)

    myfont = ImageFont.truetype('./attr.ttf',fontsize)
    # print(myfont)
    ImageDraw.Draw(images).text((2*fontsize,0),str(num),font=myfont,fill='red')
    images.save('aaa.jpg')
    images.show()


# img = Image.open("")
addNumTolmg(img='./icon.jpeg')

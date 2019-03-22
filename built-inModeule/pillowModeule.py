#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies@gmail.com
@software: pycharm
@file: pillowModeule.py
@time: 19-3-22 下午4:23
@desc:
''' 

#ImageFilter: 滤镜
# from PIL import Image,ImageFilter
#
# img = Image.open('Sierra.jpg')
# w, h = img.size
# print('Original image to: %sx%s'%(w,h))
#将图片缩放到50%
# img.thumbnail((w//2,h//2))
# print("Reszie image to :%sx%s"%(w//2,h//2))
# img.save("test.jpeg",'jpeg')
# img.show()

#应用模糊滤镜:
# img2 = img.filter(ImageFilter.BLUR)
# img2.save("blur.jpeg",'jpeg')
# img2.show()

#生成字符串验证码
from PIL import  Image,ImageDraw,ImageFont,ImageFilter
import random
#随机数字
def rndChar():
    return chr(random.randint(65,90))
#随机颜色
def rndColor():
    return (random.randint(64,255),random.randint(64,255),
            random.randint(64,255),)

#随机颜色2
def rmdColor2():
    return (random.randint(32,127),random.randint(32,127),
            random.randint(32,127),)

# 大小 240 x 60
width = 60 * 4
height = 60
#创建画布
image = Image.new("RGB",(width,height),(255,255,255))
#创建font对象
font = ImageFont.truetype("")
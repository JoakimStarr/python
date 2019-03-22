#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies@gmail.com
@software: pycharm
@file: rwFile.py
@time: 19-3-21 下午9:57
@desc: 文件读写
'''
with open("./test.txt",'rb') as f:
    print(f.read())
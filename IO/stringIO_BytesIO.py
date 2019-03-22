#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies@gmail.com
@software: pycharm
@file: stringIO_BytesIO.py
@time: 19-3-21 下午10:03
@desc:StringIO和BytesIO
''' 

#stringIO
from io import StringIO
f = StringIO("Hello!\nHi\nGoodBye")
# print(f.write("Hello stringIO"))
# print(f.write(","))
# print(f.write("this stringIO_BytesIO.py"))
# print(f.getvalue())
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

#BytesIO
# from io import BytesIO
# f = BytesIO()
# f.write("中文".encode('utf-8'))
# print(f.getvalue())
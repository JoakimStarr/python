#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies@gmail.com
@software: pycharm
@file: server..py
@time: 19-3-27 下午3:07
@desc:
'''

from wsgiref.simple_server import  make_server
from wsgl_demo import application

httpd = make_server('',8000,application)
print("Server HTTP on port 8000...")
httpd.serve_forever()

#!/usr/bin/env python
# encoding: utf-8
'''
@author: miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies123@gmail.com
@software: pycharm
@file: decorator.py
@time: 19-3-17 下午2:28
@desc:
'''
from datetime import datetime

def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print("%s %s():"% (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log("execute")
def now():
    print(datetime.now())

now()
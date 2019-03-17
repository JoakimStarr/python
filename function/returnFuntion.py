#!/usr/bin/env python
# encoding: utf-8
'''
@author: miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies123@gmail.com
@software: pycharm
@file: returnFuntion.py
@time: 19-3-17 下午2:08
@desc:
'''
def lasy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lasy_sum(1,2,3,4,5,6)
print(f)
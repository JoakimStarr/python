#!/usr/bin/env python
# encoding: utf-8
'''
@author: miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies123@gmail.com
@software: pycharm
@file: hello.py
@time: 19-3-17 下午2:40
@desc:
'''
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello world")
    elif len(args) == 2:
        print("Hello,%s"% args[1])
    else:
        print("Too many arguments")


if __name__ == '__main__':
    test()
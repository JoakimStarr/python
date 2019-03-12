#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: Miskies123@gmail.com
@software: pycharm
@file: listForData.py
@time: 19-3-12 下午11:37
@desc:
'''
class Ring(object):

    def __init__(self, l):
        if not len(l):
            raise "ring must have at least one element"
        self._data = l

    def __repr__(self):
        return repr(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, item):
        return self._data[item]

    def turn(self):
        last = self._data.pop(-1)
        self._data.insert(0,last)

    def first(self):
        return self._data[0]

    def last(self):
        return self._data[-1]

l = [{1:1},{2:2},{3:3},{4:4}]
r = Ring(l).last()
print(r)
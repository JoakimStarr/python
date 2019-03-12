#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: Miskies123@gmail.com
@software: pycharm
@file: statistics.py
@time: 19-3-12 下午11:10
@desc:
'''
class Counter(object):

    def __init__(self):
        self.dict = {}

    def add(self,item):
        count = self.dict.setdefault(item,0)
        self.dict[item] = count + 1
        # print(self.dict[item])
        # print(self.dict)

    def counts(self,desc=None):
        result = [[val,key] for (key,val) in self.dict.items()]
        result.sort()
        if desc:
            result.reverse()
        return result

if __name__ == '__main__':
    sentence = "Hello there this is a test.  Hello there this was a test, but now it is not."
    words = sentence.split()
    c = Counter()#Counter求数组中每个元素出现的次数
    for word in words:
        c.add(word)
    print("Ascending count")
    print(c.counts())
    print("Descending count")
    print(c.counts(1))
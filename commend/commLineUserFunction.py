#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: Miskies123@gmail.com
@software: pycharm
@file: commLineUserFunction.py
@time: 19-3-12 下午9:34
@desc:
'''
import unittest
import sys

class Tests(unittest.TestCase):
    def testAddOnePlusOne(self):
        assert 1 == 2

def main():
    unittest.TextTestRunner().run(test_suite())

def test_suite():
    return unittest.makeSuite(Tests,'test')

def debug():
    test_suite().debug()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        globals()[sys.argv[1]]()
    else:
        main()
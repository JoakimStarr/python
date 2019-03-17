#!/usr/bin/env python
# encoding: utf-8
'''
@author: miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies123@gmail.com
@software: pycharm
@file: demo.py
@time: 19-3-17 下午3:29
@desc:
'''

class Student(object):
    def __init__(self,name,score):
        self._name = name
        self.__score = score

    def print_score(self):
        print("%s :%s"%(self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return "C"
brat = Student("Miskies",98)
# brat.print_score()
# print(brat.get_grade())
# print(brat._name)
# print(brat._Student__score)
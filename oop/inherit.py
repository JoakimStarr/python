#!/usr/bin/env python
# encoding: utf-8
'''
@author: miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies123@gmail.com
@software: pycharm
@file: inherit.py
@time: 19-3-17 下午3:49
@desc:
'''

class Animal(object):
    def run(self):
        print("Animal is running...")
class Dog(Animal):
    def run(self):
        print("Dog is running...")
    def eat(self):
        print("Eating meat...")
class Cat(Animal):
    pass
dog = Dog()
dog.run()

cat = Cat()
cat.run()
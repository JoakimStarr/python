#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies@gmail.com
@software: pycharm
@file: serialization.py
@time: 19-3-22 下午1:46
@desc:序列化
''' 
import pickle
# d = dict(name='Miskies',age='18',score=88)
# print(pickle.dumps(d))
# with open('test.txt','wb') as f:
    # print(pickle.dump(d,f))

# with open('test.txt','rb') as f:
#     d = pickle.load(f)
#     print(d)


import json
# print(json.dumps(d))

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def studentDict(std):
    return {
        'name': std.name,
        'age' : std.age,
        'score': std.score
    }
s = Student("Miskies",18,85)
# print(json.dumps(s,default=studentDict))
print(json.dumps(s,default=lambda obj:obj.__dict__))

def dictStudent(d):
    return Student(d['name'],d["age"],d['score'])

json_str = '{"name":"Miskies","score":85,"age":18}'
print(json.loads(json_str,object_hook=dictStudent))


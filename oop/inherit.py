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
#继承
class Animal(object):
    def run(self):
        print("Animal is running...")
class RunnableMaxIn():
    pass
class Dog(Animal,RunnableMaxIn):
    def run(self):
        print("Dog is running...")
    def eat(self):
        print("Eating meat...")
class Cat(Animal):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "Student object (name=%s)"%self.name
    __repr__ = __str__

class Fib(object):
    def __init__(self):
        self.a, self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a >100000:
            raise StopIteration()
        return self.a

# __getitem__
class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n,int):
            a,b= 1,1
            for x in range(n):
                a,b= b,a+b
            return a
        if isinstance(n,slice):#n切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b =1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b, a+b
            return L

#__getattr__
class Student(object):
    def __init__(self):
        self.name = "Miskies"
    def __getattr__(self, attr):
        if attr == "age":
            return 25

#_call__
class Call(object):
    def __init__(self,name):
        self.name = name
    def __call__(self, *args, **kwargs):
        print("My name is %s"%self.name)
# c = Call("Miskies")
# print(callable(c)) #True
# print(callable(max()))

#使用枚举类
from enum import Enum,unique
Month = Enum("Month",("Jan","Fed","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov",'Dec'))
# for name,member in Month.__members__.items():
    # print(name, "==>",member,',',member.value)

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day = Weekday.Mon.value
# print(day)
for name,member in Weekday.__members__.items():
    print(name,"==>",member,member.value)

# s = Student()
# print(s.name)
# print(s.age)
# f = Fib2()
# print(f[0:500])
# print(list(f[100])[12:]

# dog = Dog()
# dog.run()

# cat = Cat()
# cat.run()

# print(Cat("Miskies"))
# print(isinstance(dog,Dog))
# Fib(5 )
# for n in Fib():
#     print(n)
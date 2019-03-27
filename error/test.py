#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 
@Author: Miskies
@LastEditors: huacong
@Date: 2019-03-19 19:14:57
@LastEditTime: 2019-03-19 19:27:03
'''
#直接打印
# def foo(s):
#     n = int(s)
#     print(">>>n = %d"%n)
#     return 10 % n
# def main():
#     foo("0")
# main()

# 断言  可以使用 -0参数关闭assert
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
# def main():
#     foo("0")
# main()

# logging
# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info("n = %d"%n)
# print(10 /n)

#pdb 启动方式：python3 -m pdb tset.py
# import pdb
# s = '0'
# n = int(s)
# pdb.set_trace()
# print(10 / n)

#单元测试


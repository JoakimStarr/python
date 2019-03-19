#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies@gmail.com
@software: pycharm
@file: errorProcess.py
@time: 19-3-19 上午10:29
@desc:
'''
#错误处理
# import logging
# def foo(s):
#     return 10 / int(s)
# def bar(s):
#     return foo(s) * 2
# def main():
#     try:
#         bar("0")
#     except Exception as e:
#         # print("Error:",e)
#         logging.exception(e)
#     finally:
#         print("finally...")
# main()
# print("END")

# try:
#     print("try...")
#     # r = 10 /0
#     r = 10 / 2
#     # r = 10 / int('a')
#     print("result:",r)
# except ValueError as e:
#     print("execpt:",e)
# except ZeroDivisionError as e:
#     print("except:",e)
# else:
#     print("No error")
# finally:
#     print("finally...")
#
# print("END")

#记录错误
#抛出错误
# class FooError(ValueError):
#     pass
# def foo(s):
#     n = int(s)
#     if n ==0 :
#         raise FooError("invalid value:%s"%s)
#     return 10 / n
# foo(0)

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError("invalid value:%s"%s )
#     return 10 / n
# def bar():
#     try:
#         foo("0")
#     except ValueError as e:
#         print("ValueError")
#         raise
# bar()


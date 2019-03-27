#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies@gmail.com
@software: pycharm
@file: process.py
@time: 19-3-22 下午2:12
@desc多进程:
''' 

# import os
#Only works on Unix/Linux/Mac 仅能在Unix/Linux/Mac上工作
# print('Process (%s) start...'%os.getpid())
# print(os.fork())
# pid = os.fork()
# if pid == 0:
#     print("I am child process (%s) and my parent is %s."%(os.getpid()))
# else:
#     print("I (%s) just created a child process (%s)."%(os.getpid(),pid))

#跨平台
# from multiprocessing import  Process
# import os
#
# def run_proc(name):
#     print("Run child process %s (%s)..."%(name,os.getpid()))
#
# if __name__ == '__main__':
#     print("Parent process %s ."%os.getpid())
#     p = Process(target=run_proc,args=('test',))
#     print("Child process will start...")
#     p.start()
#     p.join()
#     print("Child process end...")



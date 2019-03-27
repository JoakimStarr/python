#!/usr/bin/env python
# encoding: utf-8
'''
@author: miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies123@gmail.com
@software: pycharm
@file: server.py
@time: 19-3-15 下午1:40
@desc:
'''
#
# import socket
# #创建socket对象
# #SOCK_DGRAM    udp模式
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# port = ("localhost",8000)
# s.bind(port)  #绑定服务器的ip和端口
#
# while True:
#     data,addr = s.recvfrom(1024)
#     print("接收到来自%s的消息：%s"%(addr,data))
#     message = input("您要回复的消息是(输入q退出):")
#     if message == "":
#         message = input("您要回复的消息是(输入q退出):")
#     elif message == 'q':
#         break
#     else:
#         s.sendto(message.encode(),("localhost",8001))
#
# s.close()

from client import Client
import  threading

while True:
    message = input("您要发送的消息为：")
    c = Client(message=message,port=9998)
    # threading.Thread(target=c.send,name='send').start()
    c.send()
    r = Client(port=9999)
    r.receive()
    # threading.Thread(target=r.receive,name='receive').start()
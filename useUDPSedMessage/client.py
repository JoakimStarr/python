#!/usr/bin/env python
# encoding: utf-8
'''
@author: miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies123@gmail.com
@software: pycharm
@file: client.py
@time: 19-3-15 下午2:28
@desc:
'''
import socket
import threading

#创建socket对象
#SOCK_DGRAM    udp模式
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#发送数据 字节
# port = ("localhost",8000)
# s.bind(("localhost",8001))

# while True:
#     message = input("请输入要发送的消息(输入q退出)：")
#     if message == "":
#         message = input("请输入要发送的消息(输入q退出)：")
#     elif message == 'q':
#         break
#     else:
#         s.sendto(message.encode(),port)
#     data,addr=s.recvfrom(1027)
#     print("接受到来自%s的消息为%s"%(addr,data.decode()))
# s.close()

class Client(object):
    def __init__(self,message=None,issend='send''',host='localhost',port=9999):
        self.message = message
        self.issend = issend
        self.port = port
        self.host = host
        self.cliet = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    def send(self):
        # self.message=input("您要发送的消息是：")
        self.cliet.sendto(str(self.message).encode(),(self.host,self.port))
        # print(threading.current_thread().name)
        print("已发送消息：%s"%self.message)
        self.cliet.close()
    def receive(self):
        self.cliet.bind((self.host,self.port))
        self.data,self.attr = self.cliet.recvfrom(1024)
        print("接收到来自(%s)的消息：%s"%(self.attr,self.data.decode()))
        self.cliet.close()

    # def judge(self):
    #     if self.issend == 'send':
    #         self.send()
    #     elif self.issend == 'judge':
    #         self.receive()

def send(host='localhost',port=9999):
    message = input("您要发送消息是：")
    send = Client(message=message,host=host,port=port)
    send.send()

def receive(host='localhost',port=9998):
    rece = Client(host=host,port=port)
    rece.receive()

if __name__ == '__main__':
    while True:
        # message = input("您要发送的消息为：")
        # c = Client()
        # c.send()
        # send = threading.Thread(target=send)
        # r = Client(port=9998)
        # r.receive()
        # rece = threading.Thread(target=receive)
        # send.start()
        # rece.start()
        # send.join()
        # rece.join()
        send()
        receive()

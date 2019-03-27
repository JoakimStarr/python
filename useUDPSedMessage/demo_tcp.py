#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies@gmail.com
@software: pycharm
@file: demo_tcp.py
@time: 19-3-26 上午11:41
@desc:tcp编程
'''

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('www.sina.com.cn',80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\n'
       b'Connection: close\r\n\r\n')

buffer = []
while True:
    d =s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# print(data)
header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('sina.html','wb') as f:
    f.write(html)
s.close()
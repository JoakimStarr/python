#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies@gmail.com
@software: pycharm
@file: reveEmail.py
@time: 19-3-26 上午11:47
@desc:POST3收取邮件
''' 

import  poplib
email = input("Email:")
passwd = input("password:")
pop3_server = input("POP3 Server:")

server = poplib.POP3(pop3_server)

server.set_debuglevel(1)

print(server.getwelcome().deconde('utf-8'))

server.user(email)
server.pass_(passwd)

print('Message:%s,Size:%s'%server.stat())
resp,mails,octets = server.list()
print(mails)

index = len(mails)
resp,lines,octests =server.retr(index)

msg_content = b'\r\n'.join(lines).decode("utf-8")
msg = Parser().parsestr(msg_content)

server.quit()
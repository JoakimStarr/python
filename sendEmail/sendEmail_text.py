#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies@gmail.com
@software: pycharm
@file: sendEmail_text.py
@time: 19-3-26 上午11:57
@desc:发送邮件
''' 

from email.mime.text import MIMEText
import smtplib

# msg = MIMEText("Hello,send by python....")

sender = "starcloudscience@163.com"
receiver = "18385086034@163.com"
smtpserver = 'smtp.163.com'
password = 'Miskies123'
subject = 'Python send annex Email test'

s = smtplib.SMTP(sender,)
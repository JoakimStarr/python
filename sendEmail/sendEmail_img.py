#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: Miskies123@gmail.com
@software: pycharm
@file: sendEmail_img.py
@time: 19-3-12 上午11:51
@desc:
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
sender = 'starcloudscience@163.com'
recerver = '18385086034@163.com'
subject = 'python send image email test'
smptserver = 'smtp.163.com'
password = 'Miskies123'

msgRoot = MIMEMultipart('related')
msgRoot["Subject"] = 'test message'

msgText = MIMEText(u'''
    <h2>send html text and images<h2>
    <img src="./Sierra.jpg"> 
    ''','html','utf-8')
msgRoot.attach(msgText)

fp = open("./Sierra.jpg",'rb')
msgImg = MIMEImage(fp.read())
fp.close()

msgImg.add_header("Content-ID",'')
msgRoot.attach(msgImg)

try:
    smtp = smtplib.SMTP()
    smtp.connect(smptserver)
    smtp.login(sender,password)
    smtp.sendmail(sender,recerver,msgRoot.as_string())
    print("发送成功")
    smtp.quit()
except smtplib.SMTPException:
    print("发送失败")

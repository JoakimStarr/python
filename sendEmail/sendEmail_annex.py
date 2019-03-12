#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: Miskies123@gmail.com
@software: pycharm
@file: sendEmail_annex.py
@time: 19-3-12 下午9:15
@desc:
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "starcloudscience@163.com"
receiver = "18385086034@163.com"
smtpserver = 'smtp.163.com'
password = 'Miskies123'
subject = 'Python send annex Email test'

msgRoot = MIMEMultipart("mixed")
msgRoot["Subject"] = "test email"

#构造附件
attr = MIMEText(open('./Sierra.jpg','rb').read(),'base64','utf-8')
attr["Content-Type"] = 'application/octet-stream'
attr["Content-Disposition"] = 'attachment;filename="Subject.jpg"'
msgRoot.attach(attr)

try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender,password)
    smtp.sendmail(sender,receiver,msgRoot.as_string())
    print("发送成功")
    smtp.quit()
except smtplib.SMTPException:
    print("ERROR：发送失败")
#!/usr/bin/env python
# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'starcloudscience@163.com' #发件人账号
receiver = '18385086034@163.com'#收件人账号
subject = 'python email test'#主题
smtpserver = 'smtp.163.com'#发送邮件的服务器
username = 'starcloudscience@163.com'#用户名
password = 'Miskies123'#授权码不是密码

msg = MIMEText(u'你好','plain','utf-8')#发送的消息，发送普通文件时候设置为plain，字符编码
msg["From"] = sender#显示的发送热
msg['To'] = receiver#显示的收件人
msg['Subject'] = Header(subject,'utf-8')#邮件主题，
try:
    smtp = smtplib.SMTP()#创建一个连接
    smtp.connect(smtpserver)#练级发送的服务器
    smtp.login(username,password)#登录服务器
    smtp.sendmail(sender,receiver,msg.as_string())#填入邮件相关消息并发送
    print("发送成功")#发送成功提示
    smtp.quit()#退出服务器登录

except smtplib.SMTPException:
    print("ERROR:发送失败")#发送失败

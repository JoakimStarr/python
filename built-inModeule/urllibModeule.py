#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies@gmail.com
@software: pycharm
@file: urllibModeule.py
@time: 19-3-22 下午4:03
@desc:
'''
from urllib import request,parse

# with request.urlopen('https://api.douban.com/v2/book/2129650') as url:
#     data = url.read()
#     print("Status:",url.status,url.reason)
#     for k, v in url.getheaders():
#         print("%s:%s"%(k,v))
#     print("Data:",data.decode("utf-8"))


#模拟游览器发送get请求

# req = request.Request("http://www.douban.com/")
# req.add_header("User-Agent",'Mozilla/6.0 (iPhone; CPU '
#                             'iPhone OS 8_0 like Mac OS X) AppleWebKi'
#                             't/536.26 (KHTML, like Gecko) Version/8.0 '
#                             'Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print("Status:",f.status,f.reason)
#     for k, v in f.getheaders():
#         print("%s: %s"%(k,v))
#     print("Data:",f.read().decode("utf-8"))

print("Login to weibo.cn...")
email = input("Email: ")
passwd = input("Passwd: ")
login_data = parse.urlencode([
    ("username",email),
    ("password",passwd),
    ('entry','mweibo'),
    ('client_id',''),
    ('savestate','1'),
    ('ec',''),
    ('pagerefer','https://passport.weibo.cn/'
                 'signin/welcome?entry=mweibo&r'
                 '=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request("https://passport.weibo.cn/sso/login")
req.add_header("Origin","https://passport.weibo.cn")
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone '
                             'OS 8_0 like Mac OS X) AppleWebKit/536.'
                             '26 (KHTML, like Gecko) Version/8.0 Mobile'
                             '/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweib'
                          'o&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


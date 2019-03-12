#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: Miskies123@gmail.com
@software: pycharm
@file: soundex.py
@time: 19-3-12 下午9:47
@desc:
'''
def soundex(name,len=4):

    digits = '012303115487178487487487518419841498489156'
    sndx = ''
    fc = ''

    for c in name.upper():
        # print(name.upper())
        if c.isalpha():
            if not fc:
                fc = c

            print(c)
            # print(digits)
            #d的来源 digits取名字的每个字符的ASCII马减去最小的A的ASCII码的数字
            d = digits[ord(c) - ord('A')]
            # print(d)
            # print(ord(c))
            # print(ord('A'))
            # print(ord(c)-ord('A'))
            # print(digits[10])
            # print(sndx)
            # print(d)
            if not sndx or (d != sndx[-1]):
                sndx += d

    print(sndx)

    sndx = fc + sndx[1:] #取名字的第一个单词和sndx的第2为开始后面的数字
    sndx =sndx.replace('0','')#去除数字为0的
    return (sndx + (len * '0'))[:len]#在返回的结果后面加上len个0取第len个单词， 意思就是说只能输出4个字符，字符不够的后面加0

str=soundex('Knuth')
str1=soundex('Kant')
print(str)
print('\n')
print(str1)
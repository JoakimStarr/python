#!/usr/bin/env python
# encoding: utf-8
'''
@author: Miskies
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: miskies@gmail.com
@software: pycharm
@file: demo.py
@time: 19-3-18 下午3:20
@desc:
''' 
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    cv2.imshow("captrue",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

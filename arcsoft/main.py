#!/usr/bin/env python
# ! -*- coding:utf-8 -*-
# !@Author: faple
# !@Time: 2019/3/29 13:59
import face_dll, face_class
from ctypes import *
import cv2
import face_function as fun

Appkey = b'4fEUb81MxFozpgncw2k8a7ZAEArfvNGZjvvo8jZDLgkn'
SDKey = b'7ewepBAnhYgQdsGyJ9aqDchQ9aZGy8U8sYdHMHehx9ps'
# 激活
ret = fun.JH(Appkey, SDKey)
if ret == 0 or ret == 90114:
    print('激活成功:', ret)
else:
    print('激活失败:', ret)
    pass
# 初始化
ret = fun.CSH()
if ret[0] == 0:
    print('初始化成功:', ret, '句柄', fun.Handle)
else:
    print('初始化失败:', ret)
# 加载图片
im = face_class.IM()
im.filepath = 'E:/PycharmProjects/face_recognition_test/arcsoft/3.jpg'
im = fun.LoadImg(im)
print(im.filepath, im.width, im.height)
# cv2.imshow('im',im.data)
# cv2.waitKey(0)
print('加载图片完成:', im)

ret = fun.RLSB(im)
if ret[0] == -1:
    print('人脸识别失败:', ret)
    pass
else:
    print('人脸识别成功:', ret)
# 显示人脸照片
# showimg(im,ret)
# 提取单人1特征
ft = fun.getsingleface(ret[1], 0)
tz1 = fun.RLTZ(im, ft)[1]
# 提取单人2特征
# ft = fun.getsingleface(ret[1], 1)
# tz2 = fun.RLTZ(im, ft)[1]
# 特征保存到文件
fun.writeFTFile(tz1,'d:/1.dat')
# fun.writeFTFile(tz2,'d:/2.dat')
# 文件获取特征
# tz = fun.ftfromfile('d:/1.dat')
# jg = fun.BD(tz1, tz)
# print(jg[1])
# 结果比对
# jg=fun.BD(tz1,tz2)
# print(jg[1])

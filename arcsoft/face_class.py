#!/usr/bin/env python
# ! -*- coding:utf-8 -*-
# !@Author: faple
# !@Time: 2019/3/29 13:58
from ctypes import *


# 人脸框
class MRECT(Structure):
    _fields_ = [(u'left1', c_int32), (u'top1', c_int32), (u'right1', c_int32), (u'bottom1', c_int32)]


# 版本信息     版本号,构建日期,版权说明
class ASF_VERSION(Structure):
    _fields_ = [('Version', c_char_p), ('BuildDate', c_char_p), ('CopyRight', c_char_p)]


# 单人人脸信息  人脸狂,人脸角度
class ASF_SingleFaceInfo(Structure):
    _fields_ = [('faceRect', MRECT), ('faceOrient', c_int32)]


# 多人人脸信息 人脸框数组,人脸角度数组,人脸数
class ASF_MultiFaceInfo(Structure):
    # _fields_=[('faceRect',POINTER(MRECT)),('faceOrient',POINTER( c_int32)),('faceNum',c_int32)]
    _fields_ = [(u'faceRect', POINTER(MRECT)), (u'faceOrient', POINTER(c_int32)), (u'faceNum', c_int32)]
    # _fields_=[(u'faceRect',MRECT*50),(u'faceOrient',c_int32*50),(u'faceNum',c_int32)]


# 人脸特征 人脸特征,人脸特征长度
class ASF_FaceFeature(Structure):
    _fields_ = [('feature', c_void_p), ('featureSize', c_int32)]


# 自定义图片类
class IM:
    def __init__(self):
        self.filepath = None
        self.date = None
        self.width = 0
        self.height = 0

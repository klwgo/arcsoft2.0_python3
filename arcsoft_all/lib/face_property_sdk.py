#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/3/29 15:30

from . import MRECT
from ctypes import *

class ASF_AgeInfo(Structure):
    '''
    年龄信息
    ageArray: 大于0表示年龄检测结果 0表示未知
    num: 检测的人脸个数
    '''
    _fields_ = [(u'ageArray', POINTER(c_int32)), (u'num', c_int32)]

class ASF_GenderInfo(Structure):
    '''
    性别信息
    genderArray: 0表示男性， 1表示女性， -1表示未知
    '''
    _fields_ = [(u'genderArray', POINTER(c_int32)), (u'num', c_int32)]

class ASF_Face3DAngle(Structure):
    '''
    3D角度信息
    roll: 横滚角
    yaw: 偏航角
    pitch: 俯仰角
    status: 0正常， 其他数值检测结果不可信
    num: 检测的人脸个数
    '''
    _fields_ = [(u'roll', POINTER(c_float)), (u'yaw', POINTER(c_float)), (u'pitch', POINTER(c_float)), (u'status', POINTER(c_int32)), (u'num', c_int32)]
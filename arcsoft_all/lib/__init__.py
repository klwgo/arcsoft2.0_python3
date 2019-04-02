#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/3/29 14:59

from ctypes import *

# 人脸框
class MRECT(Structure):
    _fields_ = [(u'left', c_int32), (u'top', c_int32), (u'right', c_int32), (u'bottom', c_int32)]
#!/usr/bin/env python
# ! -*- coding:utf-8 -*-
# !@Author: faple
# !@Time: 2019/3/29 15:30

from ctypes import *
from . import MRECT


# 版本信息
class ASF_VERSION(Structure):
    # version版本 builddate构件日期  copyright版权说明
    _fields_ = [(u'Version', c_char_p), (u'BuildDate', c_char_p), (u'CopyRight', c_char_p)]


# 单人脸检测信息
class ASF_SingleFaceInfo(Structure):
    # faceRect 人脸框  faceOrient 人脸角度
    _fields_ = [(u'faceRect', MRECT), (u'faceOrient', c_int32)]


# 多人脸检测信息
class ASF_MultiFaceInfo(Structure):
    _fields_ = [(u'faceRect', POINTER(MRECT)), (u'faceOrient', POINTER(c_int32)), (u'faceNum', c_int32)]

# 人脸特征
class ASF_FaceFeature(Structure):
    _fields_ = [(u'feature', c_void_p), (u'featureSize', c_int32)]


# 检测方向的优先级
ASF_OP_0_ONLY = 0x1  # 仅检测0度
ASF_OP_90_ONLY = 0x2  # 仅检测90度
ASF_OP_270_ONLY = 0x3  # 仅检测270度
ASF_OP_180_ONLY = 0x4  # 仅检测180度
ASF_OP_0_HIGHER_EXT = 0x5  # 检测0, 90, 270, 180全角度

# 检测到的人脸角度(按逆时针方向)
ASF_OC_0 = 0x1  # 0 degree
ASF_OC_90 = 0x2  # 90 degree
ASF_OC_270 = 0x3  # 270 degree
ASF_OC_180 = 0x4  # 180 degree
ASF_OC_30 = 0x5  # 30 degree
ASF_OC_60 = 0x6  # 60 degree
ASF_OC_120 = 0x7  # 120 degree
ASF_OC_150 = 0x8  # 150 degree
ASF_OC_210 = 0x9 # 210 degree
ASF_OC_240 = 0xa # 240 degree
ASF_OC_300 = 0xb # 300 degree
ASF_OC_330 = 0xc # 330 degree

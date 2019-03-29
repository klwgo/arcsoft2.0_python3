#!/usr/bin/env python
# ! -*- coding:utf-8 -*-
# !@Author: faple
# !@Time: 2019/3/29 13:58
from ctypes import *
from face_class import *

wuyongdll = CDLL('E:/PycharmProjects/face_recognition_test/arcsoft/libarcsoft_face.dll')
dll = CDLL('E:/PycharmProjects/face_recognition_test/arcsoft/libarcsoft_face_engine.dll')
dllc = cdll.msvcrt
ASF_DETECT_MODE_VIDEO = 0x00000000
ASF_DETECT_MODE_IMAGE = 0xFFFFFFFF
c_ubyte_p = POINTER(c_ubyte)
# 激活
jihuo = dll.ASFActivation
jihuo.restype = c_int32
jihuo.argtypes = (c_char_p, c_char_p)
# 初始化
chushihua = dll.ASFInitEngine
chushihua.restype = c_int32
chushihua.argtypes = (c_long, c_int32, c_int32, c_int32, c_int32, POINTER(c_void_p))
# 人脸识别
shibie = dll.ASFDetectFaces
shibie.restype = c_int32
shibie.argtypes = (c_void_p, c_int32, c_int32, c_int32, POINTER(c_ubyte), POINTER(ASF_MultiFaceInfo))
# 特征提取
tezheng = dll.ASFFaceFeatureExtract
tezheng.restype = c_int32
tezheng.argtypes = (
    c_void_p, c_int32, c_int32, c_int32, POINTER(c_ubyte), POINTER(ASF_SingleFaceInfo), POINTER(ASF_FaceFeature))

# 特征比对
bidui = dll.ASFFaceFeatureCompare
bidui.restype = c_int32
bidui.argtypes = (c_void_p, POINTER(ASF_FaceFeature), POINTER(ASF_FaceFeature), POINTER(c_float))
malloc = dllc.malloc
free = dllc.free
memcpy = dllc.memcpy

malloc.restype = c_void_p
malloc.argtypes = (c_size_t,)
free.restype = None
free.argtypes = (c_void_p,)
memcpy.restype = c_void_p
memcpy.argtypes = (c_void_p, c_void_p, c_size_t)

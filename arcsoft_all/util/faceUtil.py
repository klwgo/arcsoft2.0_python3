#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/3/29 17:20

from arcsoft_all.lib import face_dll, face_detect_sdk, face_property_sdk
from ctypes import *
import cv2

handle = c_void_p()
c_ubyte_p = POINTER(c_ubyte)

class IM:
    def __init__(self):
        self.filePath = None
        self.data = None
        self.width = 0
        self.height = 0

    def __str__(self) :
        return 'filePath: ' + self.filePath + ' width: ' + str(self.width) + ' height: ' + str(self.height)


# 图片加载
def loadImage(image):
    img = cv2.imread(image.filePath)
    sp = img.shape
    img = cv2.resize(img, (sp[1] // 4 * 4, sp[0] // 4 * 4))
    sp = img.shape
    image.data = img
    image.width = sp[1]
    image.height = sp[0]
    return image

# 激活函数
def asfActivation(appId, sdkKey):
    res = face_dll.ASFActivation(appId, sdkKey)
    return res

# 初始化函数
def asfInitEngine(detectMode, detectFaceOrientPriority, detectFaceScaleVal, detectFaceMaaxNum, combinedMask):
    # detectMode [in] VIDEO模式/IMAGE模式VIDEO模式，:处理连续帧的图像数据，并返回检测结果，需要将所有图像帧的数据都传入接口进行处理；IMAGE模式:，处理单帧的图像数据，并返回检测结果
    # detectFaceOrientPriority [in] 检测脸部的角度优先值，推荐仅检测单一角度，效果更优
    # detectFaceScaleVal [in] 用于数值化表示的最小人脸尺寸，该尺寸代表人脸尺寸相对于图片长边的占比。video 模式有效值范围[2,16], Image 模式有效值范围[2,32]推荐值为 16
    # detectFaceMaxNum [in] 最大需要检测的人脸个数[1-50]
    # combinedMask [in] 用户选择需要检测的功能组合，可单个或多个
    # hEngine [out] 初始化返回的引擎handle
    res = face_dll.ASFInitEngine(detectMode, detectFaceOrientPriority, detectFaceScaleVal, detectFaceMaaxNum, combinedMask, byref(handle))
    return res, handle

# 人脸检测函数
def asfDetectFaces(image, format):
    # hEngine [in] 引擎handle
    # width [in] 图片宽度为4的倍数且大于0
    # height [in] YUYV/I420/NV21/NV12格式的图片高度为2的倍数，BGR24格式的图片高度不限制
    # format [in] 颜色空间格式
    # imgData [in] 图片数据
    # detectedFaces [out] 检测到的人脸信息
    faces = face_detect_sdk.ASF_MultiFaceInfo()
    img = image.data
    imgby = bytes(image.data)
    imgcuby = cast(imgby, c_ubyte_p)
    res = face_dll.ASFDetectFaces(handle, image.width, image.height, format, imgcuby, byref(faces))
    return res, faces

# 单人脸特征提取
def asfFaceFeatureExtract(image, format, face):
    # hEngine [in] 引擎handle
    # width [in] 图片宽度为4的倍数且大于0
    # height [in] YUYV/I420/NV21/NV12格式的图片高度为2的倍数，BGR24格式的图片高度不限制
    # format [in] 颜色空间格式
    # imgData [in] 图片数据
    # faceInfo [in] 单张人脸位置和角度信息
    # feature [out] 人脸特征
    detect = face_detect_sdk.ASF_FaceFeature()
    img = image.data
    imgby = bytes(image.data)
    # print(img)
    imgcuby = cast(imgby, c_ubyte_p)
    print(handle, image.width, image.height, format, imgcuby, face, byref(detect))
    res = face_dll.ASFFaceFeatureExtract(handle, image.width, image.height, format, imgcuby, face, byref(detect))
    if res == 0:
        retz = face_detect_sdk.ASF_FaceFeature()
        retz.featureSize = detect.featureSize
        # 必须操作内存来保留特征值,因为c++会在过程结束后自动释放内存
        retz.feature = face_dll.malloc(detect.featureSize)
        face_dll.memcpy(retz.feature, detect.feature, detect.featureSize)
        # print('提取特征成功:',detectedFaces.featureSize,mem)
        return res, retz
    else:
        return res

# 人脸匹配
def asfFaceFeatureCompare(feature1, feature2):
    # hEngine [in] 引擎handle
    # feature1 [in] 待比对的人脸特征
    # feature2 [in] 待比对的人脸特征
    # confidenceLevel [out] 比对结果，置信度数值
    score = c_float()
    res = face_dll.ASFFaceFeatureCompare(handle, byref(feature1), byref(feature2), byref(score))
    return res, score.value

# 人脸信息检测
def asfProcess(image, format, faces, mask):
    # hEngine [in] 引擎handle
    # width [in] 图片宽度为4的倍数且大于0
    # height [in] YUYV/I420/NV21/NV12格式的图片高度为2的倍数，BGR24格式的图片高度不限制
    # format [in] 颜色空间格式
    # imgData [in] 图片数据
    # detectedFaces [in] 检测到的人脸信息
    # combinedMask [in] 初始化中参数combinedMask与ASF_AGE| ASF_GENDER| ASF_FACE3DANGLE的交集的子集
    imgby = bytes(image.data)
    imgcuby = cast(imgby, c_ubyte_p)
    res = face_dll.ASFProcess(handle, image.width, image.height, format, imgcuby, byref(faces), mask)
    return res

# 获取年龄
def asfGetAge():
    # hEngine [in] 引擎handle
    # ageInfo [out] 检测到的年龄信息
    ageInfo = face_property_sdk.ASF_AgeInfo()
    res = face_dll.ASFGetAge(handle, byref(ageInfo))
    return res, ageInfo

# 获取性别
def asfGetGender():
    # hEngine [in] 引擎handle
    # genderInfo [out] 检测到的性别信息
    genderInfo = face_property_sdk.ASF_GenderInfo()
    res = face_dll.ASFGetGender(handle, genderInfo)
    return res, genderInfo

# 获取3D信息
def asfGetFace3DAngle():
    # hEngine [in] 引擎handle
    # p3DAngleInfo [out] 检测到脸部3D 角度信息
    angle3Dinfo = face_property_sdk.ASF_Face3DAngle()
    res = face_dll.ASFGetFace3DAngle(handle, angle3Dinfo)
    return res, angle3Dinfo

# 获取版本信息
def asfGetVersion():
    # 成功返回版本信息，否则返回MNull。
    version = face_detect_sdk.ASF_VERSION()
    res = face_dll.ASFGetVersion(handle)
    return res, version


def getSingleFaceInfo(faces, index):
    face = face_detect_sdk.ASF_SingleFaceInfo()
    face.faceRect.left = faces.faceRect[index].left
    face.faceRect.right = faces.faceRect[index].right
    face.faceRect.top = faces.faceRect[index].top
    face.faceRect.bottom = faces.faceRect[index].bottom
    face.faceOrient = faces.faceOrient[index]
    print(face.faceRect, face.faceRect.left, face.faceRect.right, face.faceRect.top, face.faceRect.bottom,face.faceOrient)
    return face
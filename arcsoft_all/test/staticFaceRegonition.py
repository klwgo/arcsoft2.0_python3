#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/4/1 16:35
from arcsoft_all.util import faceUtil, configUtil
import os
from arcsoft_all.exception import error


# 静态图片单脸识别

# 激活引擎
def activation():
    APP_ID = configUtil.getValue('arcsoft', 'APP_ID').encode()
    SDK_KEY = configUtil.getValue('arcsoft', 'SDK_KEY').encode()
    res = faceUtil.asfActivation(APP_ID, SDK_KEY)
    if res == 0 or res == 90114:
        print('激活成功', res)
    else:
        raise error.BaseException('激活失败:' + configUtil.getValue('error_code',str(res)))

# 初始化引擎
def initEngine(detectMode = 0xFFFFFFFF, detectFaceOrientPriority = 0x5, detectFaceScaleVal = 16, detectFaceMaxNum = 50, combinedMask = 1 | 4 | 8 | 16 | 32):
    res = faceUtil.asfInitEngine(detectMode, detectFaceOrientPriority, detectFaceScaleVal, detectFaceMaxNum, combinedMask)
    if res[0] == 0:
        print('初始化成功：', res[0])
    else:
        raise error.BaseException('初始化失败：' + configUtil.getValue('error_code', res[0]))

# 加载人脸库, 获取所有人脸的特征集合
def loadFaceDatebase(path):
    images = os.listdir(path)
    # 存放特征库
    retzs = {}
    if(len(images) > 0):
        for image in images:
            img = faceUtil.IM()
            img.filePath = os.path.join(path, image)
            print(img.filePath)
            im = faceUtil.loadImage(img)
            res, faces1 = faceUtil.asfDetectFaces(im, 0x201)
            if res == 0:
                print(im.filePath, res, faces1.faceNum, faces1.faceRect)
                res1 = faceUtil.asfFaceFeatureExtract(im, 0x201, faceUtil.getSingleFaceInfo(faces1, 0))
                if res1[0] == 0:
                    print('人脸获取特征成功')
                    retzs[img.filePath] = res1[1]
                else:
                    print(error.BaseException(img.filePath + '人脸获取特征失败：' + configUtil.getValue('error_code', str(res1[0]))))
            else:
                print(error.BaseException(img.filePath + '人脸检测失败：' + configUtil.getValue('error_code', str(res))))
    return retzs

# 获取單張圖片所有人脸特征
def getFacesRET(path):
    retz = {}
    img = faceUtil.IM()
    img.filePath = path
    im = faceUtil.loadImage(img)
    res, faces1 = faceUtil.asfDetectFaces(im, 0x201)
    if res == 0:
        print(im.filePath, res, faces1.faceNum, faces1.faceRect)
        for i in range(faces1.faceNum):
            res1 = faceUtil.asfFaceFeatureExtract(im, 0x201, faceUtil.getSingleFaceInfo(faces1, i))
            if res1[0] == 0:
                print('人脸获取特征成功')
                retz[i] = res1[1]
            else:
                print(error.BaseException(img.filePath + '人脸获取特征失败：' + configUtil.getValue('error_code', str(res1[0]))))
    else:
        print(error.BaseException(img.filePath + '人脸检测失败：' + configUtil.getValue('error_code', str(res))))
    return retz


def getFacesProperty(path):
    retz = {}
    img = faceUtil.IM()
    img.filePath = path
    im = faceUtil.loadImage(img)
    res, faces1 = faceUtil.asfDetectFaces(im, 0x201)
    if res == 0:
        print(im.filePath, res, faces1.faceNum, faces1.faceRect)
        res1 = faceUtil.asfProcess(im, 0x201, faces1, 56)
        if res1 == 0:
            for i in range(faces1.faceNum):
                print(faceUtil.asfGetAge()[1].ageArray[i])
                print(faceUtil.asfGetGender()[1].genderArray[i])
                print(faceUtil.asfGetFace3DAngle()[1].roll[i])
        else:
            print(error.BaseException(img.filePath + '人脸屬性检测失败：' + configUtil.getValue('error_code', str(res1))))
    else:
        print(error.BaseException(img.filePath + '人脸检测失败：' + configUtil.getValue('error_code', str(res))))

#     res, score = faceUtil.asfFaceFeatureCompare(res1[1], res2[1])
# 測試
def test():
    activation()
    initEngine()
    retzs = loadFaceDatebase("E:/PycharmProjects/face_recognition_test/img/dataset")
    retz = getFacesRET("E:/PycharmProjects/face_recognition_test/img/input/aaa.jpeg")
    print(retz,'---')
    if len(retz) > 0:
        for i in list(retz.keys()):
            if len(retzs) > 0:
                for key in list(retzs.keys()):
                    res, score = faceUtil.asfFaceFeatureCompare(retzs[key], retz[i])
                    if res == 0:
                        if score > 0.75:
                            print(i, key, score)
    else:
        print('==============')

# test()

def test1():
    activation()
    initEngine()
    getFacesProperty("E:/PycharmProjects/face_recognition_test/img/input/aaa.jpeg")

test1()
# APP_ID = b'4fEUb81MxFozpgncw2k8a7ZAEArfvNGZjvvo8jZDLgkn'
# SDK_KEY = b'7ewepBAnhYgQdsGyJ9aqDchQ9aZGy8U8sYdHMHehx9ps'
#
# # Appkey = b'4fEUb81MxFozpgncw2k8a7ZAEArfvNGZjvvo8jZDLgkn'
# # SDKey = b'7ewepBAnhYgQdsGyJ9aqDchQ9aZGy8U8sYdHMHehx9ps'
#
# img1 = faceUtil.IM()
# img2 = faceUtil.IM()
#
# img1.filePath = 'E:/PycharmProjects/face_recognition_test/arcsoft_all/3.jpg'
# img2.filePath = 'E:/PycharmProjects/face_recognition_test/arcsoft_all/6.jpg'
#
# # 激活设备
# res = faceUtil.asfActivation(APP_ID, SDK_KEY)
# if res == 0 or res == 90114:
#     print("激活成功！", res)
# else:
#     print("激活失败！", res)
#
# # 0xFFFFFFFF, 0x1, 16, 50, 5, byref(Handle))
# res, faceEngine = faceUtil.asfInitEngine(0xFFFFFFFF, 0x5, 16, 50, 61)
# if res == 0:
#     print("初始化成功！", res)
# else:
#     print("初始化失败！", res)
#
# image1 = faceUtil.loadImage(img1)
# image2 = faceUtil.loadImage(img2)
#
# print('image1: ', image1)
# print('image2: ', image2)
# # 分开检测以及获取属性
# def test():
#     res1, faces1 = faceUtil.asfDetectFaces(image1, 0x201)
#     if res1 == 0:
#         print('image1:', res1, faces1.faceNum, faces1.faceRect)
#     else:
#         print('image1:', res1)
#     res1 = faceUtil.asfFaceFeatureExtract(image1, 0x201, faceUtil.getSingleFaceInfo(faces1, 0))
#     print('image1:', res1)
#
#     # 获取人脸属性
#     # print(1 | 4)
#     # print(8 | 16 | 32)
#     res = faceUtil.asfProcess(image1, 0x201, faces1, 56)
#     print(res)
#     print(faceUtil.asfGetAge()[1].ageArray[0])
#     print(faceUtil.asfGetGender()[1].genderArray[0])
#     print(faceUtil.asfGetFace3DAngle()[1].roll[0])
#
#     res2, faces2 = faceUtil.asfDetectFaces(image2, 0x201)
#     if res2 == 0:
#         print('image2:', res2, faces2.faceNum, faces2.faceRect)
#     else:
#         print('image2:', res2)
#     res2 = faceUtil.asfFaceFeatureExtract(image2, 0x201, faceUtil.getSingleFaceInfo(faces2, 0))
#     print('image2:', res2)
#
#     # 人脸比对
#     res, score = faceUtil.asfFaceFeatureCompare(res1[1], res2[1])
#     print(res, score)







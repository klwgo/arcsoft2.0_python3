#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/4/1 10:59
from arcsoft_all.lib import face_dll, face_detect_sdk, face_property_sdk
from arcsoft_all.util import faceUtil

APP_ID = b'4fEUb81MxFozpgncw2k8a7ZAEArfvNGZjvvo8jZDLgkn'
SDK_KEY = b'7ewepBAnhYgQdsGyJ9aqDchQ9aZGy8U8sYdHMHehx9ps'

# Appkey = b'4fEUb81MxFozpgncw2k8a7ZAEArfvNGZjvvo8jZDLgkn'
# SDKey = b'7ewepBAnhYgQdsGyJ9aqDchQ9aZGy8U8sYdHMHehx9ps'

img1 = faceUtil.IM()
img2 = faceUtil.IM()

img1.filePath = 'E:/PycharmProjects/face_recognition_test/arcsoft_all/3.jpg'
img2.filePath = 'E:/PycharmProjects/face_recognition_test/arcsoft_all/6.jpg'

# 激活设备
res = faceUtil.asfActivation(APP_ID, SDK_KEY)
if res == 0 or res == 90114:
    print("激活成功！", res)
else:
    print("激活失败！", res)

# 0xFFFFFFFF, 0x1, 16, 50, 5, byref(Handle))
res, faceEngine = faceUtil.asfInitEngine(0xFFFFFFFF, 0x5, 16, 50, 61)
if res == 0:
    print("初始化成功！", res)
else:
    print("初始化失败！", res)

image1 = faceUtil.loadImage(img1)
image2 = faceUtil.loadImage(img2)

print('image1: ', image1)
print('image2: ', image2)
# 分开检测以及获取属性
def test():
    res1, faces1 = faceUtil.asfDetectFaces(image1, 0x201)
    if res1 == 0:
        print('image1:', res1, faces1.faceNum, faces1.faceRect)
    else:
        print('image1:', res1)
    res1 = faceUtil.asfFaceFeatureExtract(image1, 0x201, faceUtil.getSingleFaceInfo(faces1, 0))
    print('image1:', res1)

    # 获取人脸属性
    # print(1 | 4)
    # print(8 | 16 | 32)
    res = faceUtil.asfProcess(image1, 0x201, faces1, 56)
    print(res)
    print(faceUtil.asfGetAge()[1].ageArray[0])
    print(faceUtil.asfGetGender()[1].genderArray[0])
    print(faceUtil.asfGetFace3DAngle()[1].roll[0])

    res2, faces2 = faceUtil.asfDetectFaces(image2, 0x201)
    if res2 == 0:
        print('image2:', res2, faces2.faceNum, faces2.faceRect)
    else:
        print('image2:', res2)
    res2 = faceUtil.asfFaceFeatureExtract(image2, 0x201, faceUtil.getSingleFaceInfo(faces2, 0))
    print('image2:', res2)

    # 人脸比对
    res, score = faceUtil.asfFaceFeatureCompare(res1[1], res2[1])
    print(res, score)

test()

# 连续检测有问题 应该是有单脸和多脸获取RECT时的指针问题
def test1():
    # 检测人脸
    res1, faces1 = faceUtil.asfDetectFaces(image1, 0x201)
    if res1 == 0:
        print('image1:', res1, faces1.faceNum, faces1.faceRect)
    else:
        print('image1:', res1)

    res2, faces2 = faceUtil.asfDetectFaces(image2, 0x201)
    if res2 == 0:
        print('image2:', res2, faces2.faceNum, faces2.faceRect)
    else:
        print('image2:', res2)

    # 测试多张人脸如何获取值
    # img3 = faceUtil.IM()
    # img3.filePath = 'E:/PycharmProjects/face_recognition_test/arcsoft_all/aaa.jpeg'
    # image3 = faceUtil.loadImage(img3)
    # res3, faces3 = faceUtil.asfDetectFaces(image3, 0x201)
    # print(faces3.faceOrient[1], faces3.faceRect[0])
    # 获取人脸特征， 先单脸
    # res1, detect1 = faceUtil.asfFaceFeatureExtract(image1, 0x201, face_detect_sdk.ASF_SingleFaceInfo(faces1.faceRect.contents, faces1.faceOrient.contents))
    res1 = faceUtil.asfFaceFeatureExtract(image1, 0x201, faceUtil.getSingleFaceInfo(faces1, 0))
    print('image1:', res1)
    # res2, detect2 = faceUtil.asfFaceFeatureExtract(image2, 0x201, face_detect_sdk.ASF_SingleFaceInfo(faces2.faceRect.contents, faces2.faceOrient.contents))
    # res2 = faceUtil.asfFaceFeatureExtract(image2, 0x201, faceUtil.getSingleFaceInfo(faces2, 0))
    # print('image2:', res2)

    # 人脸比对
    # res, score = faceUtil.asfFaceFeatureCompare(detect1, detect2)
    # print(res, score)









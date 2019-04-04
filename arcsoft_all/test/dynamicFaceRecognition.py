#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/4/4 9:09

from arcsoft_all.util import faceUtil, configUtil
import os
from arcsoft_all.exception import error
import cv2


# 获取RTSP视频流
# cap = cv2.VideoCapture("rtsp://admin:briup2017@192.168.1.120")
cap = cv2.VideoCapture(0)
# 所有的人脸
total_faces = []

# 关闭资源
def destroyCapAndCV2():
    cap.release()
    cv2.destroyAllWindows()

# 激活引擎
def activation():
    APP_ID = configUtil.getValue('arcsoft', 'APP_ID').encode()
    SDK_KEY = configUtil.getValue('arcsoft', 'SDK_KEY').encode()
    res = faceUtil.asfActivation(APP_ID, SDK_KEY)
    if res == 0 or res == 90114:
        print('激活成功', res)
    else:
        print(error.BaseException('激活失败:' + configUtil.getValue('error_code',str(res))))

# 初始化引擎
def initEngine(detectMode = 0xFFFFFFFF, detectFaceOrientPriority = 0x5, detectFaceScaleVal = 16, detectFaceMaxNum = 50, combinedMask = 1 | 4 | 8 | 16 | 32):
    res = faceUtil.asfInitEngine(detectMode, detectFaceOrientPriority, detectFaceScaleVal, detectFaceMaxNum, combinedMask)
    if res[0] == 0:
        print('初始化成功：', res[0])
    else:
        print(error.BaseException('初始化失败：' + configUtil.getValue('error_code', res[0])))
# 加载本地人脸库, 获取所有人脸的特征集合
def loadLocalFaceDatebase(path):
    images = os.listdir(path)
    # 存放特征库
    retzs = {}
    if(len(images) > 0):
        for image in images:
            img = faceUtil.IM()
            img.filePath = os.path.join(path, image)
            img.fileName = image.split('.')[0]
            # print(img.filePath)
            im = faceUtil.loadImage(img)
            res, faces1 = faceUtil.asfDetectFaces(im, 0x201)
            if res == 0:
                # print(im.filePath, res, faces1.faceNum, faces1.faceRect)
                res1 = faceUtil.asfFaceFeatureExtract(im, 0x201, faceUtil.getSingleFaceInfo(faces1, 0))
                if res1[0] == 0:
                    print(img.filePath + ' 人脸获取特征成功')
                    retzs[img.fileName] = res1[1]
                else:
                    print(error.BaseException(img.filePath + '人脸获取特征失败：' + configUtil.getValue('error_code', str(res1[0]))))
            else:
                print(error.BaseException(img.filePath + '人脸检测失败：' + configUtil.getValue('error_code', str(res))))
    return retzs

# 加载在线人脸库, 获取所有人脸的特征集合
def loadOnlineFaceDatebase(users):
    # 存放特征库
    retzs = {}
    if(len(users) > 0):
        for user in users:
            img = faceUtil.IM()
            img.filePath = user.imgUrl
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

# 获取每帧所有人脸特征
def getFacesRET(frame):
    retz = {}
    img = faceUtil.IM()
    img.filePath = ""
    img.data = frame
    im = faceUtil.loadImage(img)
    res, faces1 = faceUtil.asfDetectFaces(im, 0x201)
    if res == 0:
        print(im.filePath, res, faces1.faceNum, faces1.faceRect)
        for i in range(faces1.faceNum):
            res1 = faceUtil.asfFaceFeatureExtract(im, 0x201, faceUtil.getSingleFaceInfo(faces1, i))
            if res1[0] == 0:
                print('人脸获取特征成功')
                retz[i] = (faces1.faceRect[i], res1[1])
            else:
                print(error.BaseException(img.filePath + '人脸获取特征失败：' + configUtil.getValue('error_code', str(res1[0]))))
    else:
        print(error.BaseException(img.filePath + '人脸检测失败：' + configUtil.getValue('error_code', str(res))))
    return retz
# 测试数据库
class User:
    def __init__(self, id, name, gender, age, address, imgUrl):
        self.id = str(id)
        self.name = name
        self.gender = gender
        self.age = str(age)
        self.address = address
        self.imgUrl = imgUrl

    def __str__(self):
        return "id: " + self.id + ", name: " + self.name + ", gender: " + self.gender + ", age: " + self.age + ", address: " + self.address + ", imgUrl: " + self.imgUrl

# 在线获取所有图片
def getAllUsers():
    import pymysql
    db = pymysql.Connect(host=configUtil.getValue('datasource', 'host'), user=configUtil.getValue('datasource', 'username'), password=configUtil.getValue('datasource', 'password'), database=configUtil.getValue('datasource', 'db_name'))
    cursor = db.cursor()
    print(cursor)
    sql = "select * from faceinfo"
    users = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            user = User(row[0], row[1], row[2], row[3], "", row[5])
            users.append(user)
    except:
        print('不能获取数据！')
    db.close()
    return users

def test():
    activation()
    initEngine()
    # print(cap.get(3))
    cap.set(3, 640)
    cap.set(4, 360)
    # retzs = loadOnlineFaceDatebase(getAllUsers())
    retzs = loadLocalFaceDatebase("E:/PycharmProjects/face_recognition_test/img/dataset")
    while True:
        ret, frame = cap.read()
        if frame is None:
            print(frame)
            continue
        retz = getFacesRET(frame)
        if len(retz) > 0:
            for i in list(retz.keys()):
                cv2.rectangle(frame, (retz[i][0].left, retz[i][0].top), (retz[i][0].right, retz[i][0].bottom), (0, 0, 255), 2)
                name = "unknown"
                max = 0.0
                if len(retzs) > 0:
                    for key in list(retzs.keys()):
                        res, score = faceUtil.asfFaceFeatureCompare(retzs[key], retz[i][1])
                        if res == 0:
                            if score > max:
                                max = score
                                name = key
                print(name, max)
                if max < 0.6:
                    name = "unknown"
                # 画出一个带名字的标签，放在框下
                cv2.rectangle(frame, (retz[i][0].left - 15, retz[i][0].top + 120),
                              (retz[i][0].right + 15, retz[i][0].bottom), (187, 255, 255),
                              cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (retz[i][0].left - 10, retz[i][0].bottom), font, 1.0,
                            (0, 0, 0), 1)

        else:
            print('没有检测到人脸')

        cv2.imshow("rtsp", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    destroyCapAndCV2()

test()
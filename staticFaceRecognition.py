#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/3/22 9:37

import face_recognition
import os

# 图片存放目录
dataset = 'img/dataset'
input = 'img/input'

total_image_name = [] # 照片名: 人名_id
total_face_encoding = [] # 人脸库的脸部集合


def getAllFaceEncoding(path):
    for img in os.listdir(dataset):
        known_image = face_recognition.load_image_file(dataset+'/'+img) # 加载图片
        # face_locations = face_recognition.face_locations(image)  # 获取人脸
        # print(img, known_image)
        known_encodings = face_recognition.face_encodings(known_image) # 对脸进行编码
        if len(known_encodings) > 0:
            total_face_encoding.append(known_encodings[0])
            total_image_name.append(img[:(len(img) - 4)])


def getUnknownEncoding(path):
    unknown_image = face_recognition.load_image_file(input + '/aaa.jpeg')
    unknown_encodings = face_recognition.face_encodings(unknown_image)
    return unknown_encodings

def getName(unknown_encoding):
    for i, v in enumerate(total_face_encoding):
        # 比较2幅图片， tolerance越小越严格
        match = face_recognition.compare_faces([v], unknown_encoding, tolerance=0.4)
        # name = 'unknown'
        if match[0]:
            print(total_image_name[i])
        # else:
        #     print(name)
def main():
    getAllFaceEncoding(None)
    unknown_encodings = getUnknownEncoding(None)
    for unknown_encoding in unknown_encodings:
        getName(unknown_encoding)

if __name__ == '__main__':
    main()
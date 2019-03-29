#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/3/29 11:26
#!/usr/bin/env python
# ! -*- coding:utf-8 -*-
# !@Author: faple
# !@Time: 2019/3/29 9:29

# 人脸识别类：使用face_recognition

import cv2
import face_recognition
import os
from multiprocessing import Pool, Value, Process

# 人脸库目录
face_datasets_path = "img/input"
# 获取RTSP视频流
cap = cv2.VideoCapture("rtsp://admin:briup2017@192.168.1.120")
# 所有的文件名
total_img_names = []
# 所有的人脸
total_img_faces = []


# 判断加载人脸库时是否是合适的照片
def isImage(path, filename, num):
    face_location = face_recognition.load_image_file(path + "/" + filename)
    if len(face_location) > 0:
        # 若合适取128特征点之后加入人脸库
        total_img_faces.append(
            face_recognition.face_encodings(
                face_location)[0])
        # 文件名加入所有人名库之中
        filename = filename.split('.')[0]
        total_img_names.append(filename)
        print('人脸库中加入第' + str(num) + '张人脸：', filename)


# 加载人脸库
def loadImage():
    for filename, num in zip(os.listdir(path=face_datasets_path), range(1, len(face_datasets_path) + 1)):
        isImage(face_datasets_path, filename, num)


# 关闭资源
def destroyCapAndCV2():
    cap.release()
    cv2.destroyAllWindows()


# 获取每帧人脸信息并且进行匹配
def getFaceInformation(frame, count, total_img_faces, total_img_names):
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    # 在这个视频帧中循环遍历每个人脸
    j = 0
    for (top, right, bottom, left), face_encoding in zip(
            face_locations, face_encodings):
        j += 1
        print("===========第" + str(count) + "次人脸识别开始===============")
        print("===========第" + str(count) + "次人脸识别中=====第" + str(j) + "张人脸识别开始==========")
        # 看看面部是否与已知人脸相匹配。
        # print("===========第" + str(c) + "次人脸识别开始匹配===============", len(total_face_encoding))
        for i, v in enumerate(total_img_faces):
            match = face_recognition.compare_faces(
                [v], face_encoding, tolerance=0.45)
            name = "Unknown"
            if match[0]:
                name = total_img_names[i]
                print("===========第" + str(count) + "次人脸识别中=====第" + str(i) + "次人脸库图片比较==========", name)
                break
            print("===========第" + str(count) + "次人脸识别中=====第" + str(i) + "次人脸库图片比较==========", name)
        print("===========第" + str(count) + "次人脸识别中=====第" + str(j) + "张人脸识别结束==========")

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # 画出一个带名字的标签，放在框下
        cv2.rectangle(frame, (left - 15, bottom + 35), (right + 15, bottom), (187, 255, 255),
                      cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left - 10, bottom + 30), font, 1.0,
                    (0, 0, 0), 1)
    cv2.imwrite(str(count).split('.')[0] + '.png', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
    print("===========第" + str(count) + "次人脸识别结束===============")


# # 画出一个框，框住脸
# cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
# # 画出一个带名字的标签，放在框下
# cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255),
#               cv2.FILLED)
# font = cv2.FONT_HERSHEY_DUPLEX
# cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0,
#             (255, 255, 255), 1)

# 测试
def test1():
    # 用于多进程之间共享值
    value = Value("d", 0)
    loadImage()
    # 开启三个进程
    pool = Pool(3)
    while True:
        value.value += 1
        ret, frame = cap.read()
        if frame is None:
            continue
        pool.apply_async(func=getFaceInformation, args=(frame, value.value, total_img_faces, total_img_names))
        cv2.imshow("rtsp", frame)
        # 退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    destroyCapAndCV2()


# test1()
if __name__ == '__main__':
    test1()

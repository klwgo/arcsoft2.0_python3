#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/3/29 16:15

from ctypes import *
from .face_detect_sdk import *
from .face_property_sdk import *

wuyongdll = CDLL('E:/PycharmProjects/face_recognition_test/arcsoft_all/libarcsoft_face.dll')
dll = CDLL('E:/PycharmProjects/face_recognition_test/arcsoft_all/libarcsoft_face_engine.dll')
dllc = cdll.msvcrt
ASF_DETECT_MODE_VIDEO = 0x00000000
ASF_DETECT_MODE_IMAGE = 0xFFFFFFFF
c_ubyte_p = POINTER(c_ubyte)
# print(dll.ASF_FACE_DETECT | dll.ASF_FACERECOGNITION | dll.ASF_AGE | dll.ASF_GENDER | dll.ASF_FACE3DANGLE | dll.ASF_LIVENESS)
# 激活SDK
ASFActivation = dll.ASFActivation
# 成功返回MOK或MERR_ASF_ALREADY_ACTIVATED，否则返回失败codes。
ASFActivation.restype = c_int32
# AppId 官网获取的APPID SDKKey 官网获取的SDKKEY
ASFActivation.argtypes = (c_char_p, c_char_p)

# 初始化引擎
ASFInitEngine = dll.ASFInitEngine
# 成功返回MOK，否则返回失败codes。
ASFInitEngine.restype = c_int32
# detectMode [in] VIDEO模式/IMAGE模式VIDEO模式，:处理连续帧的图像数据，并返回检测结果，需要将所有图像帧的数据都传入接口进行处理；IMAGE模式:，处理单帧的图像数据，并返回检测结果
# detectFaceOrientPriority [in] 检测脸部的角度优先值，推荐仅检测单一角度，效果更优
# detectFaceScaleVal [in] 用于数值化表示的最小人脸尺寸，该尺寸代表人脸尺寸相对于图片长边的占比。video 模式有效值范围[2,16], Image 模式有效值范围[2,32]推荐值为 16
# detectFaceMaxNum [in] 最大需要检测的人脸个数[1-50]
# combinedMask [in] 用户选择需要检测的功能组合，可单个或多个
# hEngine [out] 初始化返回的引擎handle
ASFInitEngine.argtypes = (c_long, c_int32, c_int32, c_int32, c_int32, POINTER(c_void_p))

# 人脸检测
ASFDetectFaces = dll.ASFDetectFaces
# 成功返回MOK，否则返回失败codes。
ASFDetectFaces.restype = c_int32
# hEngine [in] 引擎handle
# width [in] 图片宽度为4的倍数且大于0
# height [in] YUYV/I420/NV21/NV12格式的图片高度为2的倍数，BGR24格式的图片高度不限制
# format [in] 颜色空间格式
# imgData [in] 图片数据
# detectedFaces [out] 检测到的人脸信息
ASFDetectFaces.argtypes = (c_void_p, c_int32, c_int32, c_int32, c_ubyte_p, POINTER(ASF_MultiFaceInfo))

# 单人脸特征提取
ASFFaceFeatureExtract = dll.ASFFaceFeatureExtract
# 成功返回MOK，否则返回失败codes。
ASFFaceFeatureExtract.restype = c_int32
#hEngine [in] 引擎handle
#width [in] 图片宽度为4的倍数且大于0
#height [in] YUYV/I420/NV21/NV12格式的图片高度为2的倍数，BGR24格式的图片高度不限制
#format [in] 颜色空间格式
#imgData [in] 图片数据
#faceInfo [in] 单张人脸位置和角度信息
#feature [out] 人脸特征
ASFFaceFeatureExtract.argtypes = (c_void_p, c_int32, c_int32, c_int32, c_ubyte_p, POINTER(ASF_SingleFaceInfo), POINTER(ASF_FaceFeature))

# 人脸特征比对
ASFFaceFeatureCompare = dll.ASFFaceFeatureCompare
# 成功返回MOK，否则返回失败codes。
ASFFaceFeatureCompare.restype = c_int32
# hEngine [in] 引擎handle
# feature1 [in] 待比对的人脸特征
# feature2 [in] 待比对的人脸特征
# confidenceLevel [out] 比对结果，置信度数值
ASFFaceFeatureCompare.argtypes = (c_void_p, POINTER(ASF_FaceFeature), POINTER(ASF_FaceFeature), POINTER(c_float))

# 人脸信息检测（年龄/性别/人脸3D角度），最多支持4张人脸信息检测，超过部分返回未知。
ASFProcess = dll.ASFProcess
# 成功返回MOK，否则返回失败codes。
ASFProcess.restype = c_int32
# hEngine [in] 引擎handle
# width [in] 图片宽度为4的倍数且大于0
# height [in] YUYV/I420/NV21/NV12格式的图片高度为2的倍数，BGR24格式的图片高度不限制
# format [in] 颜色空间格式
# imgData [in] 图片数据
# detectedFaces [in] 检测到的人脸信息
# combinedMask [in] 初始化中参数combinedMask与ASF_AGE| ASF_GENDER| ASF_FACE3DANGLE的交集的子集
ASFProcess.argtypes = (c_void_p, c_int32, c_int32, c_int32, c_ubyte_p, POINTER(ASF_MultiFaceInfo), c_int32)

# 获取年龄信息
ASFGetAge = dll.ASFGetAge
# 成功返回MOK，否则返回失败codes。
ASFGetAge.restype = c_int32
# hEngine [in] 引擎handle
# ageInfo [out] 检测到的年龄信息
ASFGetAge.argtypes = (c_void_p, POINTER(ASF_AgeInfo))

# 获取性别信息
# ASFGetGender
ASFGetGender = dll.ASFGetGender
# 成功返回MOK，否则返回失败codes。
ASFGetGender.restype = c_int32
# hEngine [in] 引擎handle
# genderInfo [out] 检测到的性别信息
ASFGetGender.argtypes = (c_void_p, POINTER(ASF_GenderInfo))

# 获取3D角度信息
ASFGetFace3DAngle = dll.ASFGetFace3DAngle
# 成功返回MOK，否则返回失败codes。
ASFGetFace3DAngle.restype = c_int32
# hEngine [in] 引擎handle
# p3DAngleInfo [out] 检测到脸部3D 角度信息
ASFGetFace3DAngle.argtypes = (c_void_p, POINTER(ASF_Face3DAngle))

# 获取版本信息。
ASFGetVersion = dll.ASFGetVersion
# 成功返回版本信息，否则返回MNull。
ASFGetVersion.restype = POINTER(ASF_VERSION)
# hEngine [in] 引擎handle
ASFGetVersion.argtypes = (c_void_p,)

malloc = dllc.malloc
free = dllc.free
memcpy = dllc.memcpy
malloc.restype = c_void_p
malloc.argtypes = (c_size_t,)
free.restype = None
free.argtypes = (c_void_p,)
memcpy.restype = c_void_p
memcpy.argtypes = (c_void_p, c_void_p, c_size_t)

# 错误码名 十六进制 十进制 错误码说明
# MOK 0 0 成功
# MERR_UNKNOWN 1 1 错误原因不明
# MERR_INVALID_PARAM 2 2 无效的参数
# MERR_UNSUPPORTED 3 3 引擎不支持
# MERR_NO_MEMORY 4 4 内存不足
# MERR_BAD_STATE 5 5 状态错误
# MERR_USER_CANCEL 6 6 用户取消相关操作
# MERR_EXPIRED 7 7 操作时间过期
# MERR_USER_PAUSE 8 8 用户暂停操作
# MERR_BUFFER_OVERFLOW 9 9 缓冲上溢
# MERR_BUFFER_UNDERFLOW A 10缓冲下溢
# MERR_NO_DISKSPACE B 11 存贮空间不足
# MERR_COMPONENT_NOT_EXIST C 12 组件不存在
# MERR_GLOBAL_DATA_NOT_EXIST D 13 全局数据不存在
# MERR_FSDK_INVALID_APP_ID 7001 28673 无效的App Id
# MERR_FSDK_INVALID_SDK_ID 7002 28674 无效的SDK key
# MERR_FSDK_INVALID_ID_PAIR 7003 28675 AppId和SDKKey不匹配
# MERR_FSDK_MISMATCH_ID_AND_SDK 7004 28676 SDKKey和使用的SDK不匹配
# MERR_FSDK_SYSTEM_VERSION_UNSUPPORTED 7005 28677 系统版本不被当前SDK所支持
# MERR_FSDK_LICENCE_EXPIRED 7006 28678 SDK有效期过期，需要重新下载更新
# MERR_FSDK_FR_INVALID_MEMORY_INFO 12001 73729 无效的输入内存
# MERR_FSDK_FR_INVALID_IMAGE_INFO 12002 73730 无效的输入图像参数
# MERR_FSDK_FR_INVALID_FACE_INFO 12003 73731 无效的脸部信息
# MERR_FSDK_FR_NO_GPU_AVAILABLE 12004 73732 当前设备无GPU可用
# MERR_FSDK_FR_MISMATCHED_FEATURE_LEVEL 12005 73733 待比较的两个人脸特征的版本不一致
# MERR_FSDK_FACEFEATURE_UNKNOWN 14001 81921 人脸特征检测错误未知
# MERR_FSDK_FACEFEATURE_MEMORY 14002 81922 人脸特征检测内存错误
# MERR_FSDK_FACEFEATURE_INVALID_FORMAT 14003 81923 人脸特征检测格式错误
# MERR_FSDK_FACEFEATURE_INVALID_PARAM 14004 81924 人脸特征检测参数错误
# MERR_FSDK_FACEFEATURE_LOW_CONFIDENCE_LEVEL 14005 81925 人脸特征检测结果置信度低
# MERR_ASF_EX_FEATURE_UNSUPPORTED_ON_INIT 15001 86017 Engine不支持的检测属性
# MERR_ASF_EX_FEATURE_UNINITED 15002 86018 需要检测的属性未初始化
# MERR_ASF_EX_FEATURE_UNPROCESSED 15003 86019 待获取的属性未在process中处理过
# MERR_ASF_EX_FEATURE_UNSUPPORTED_ON_PROCESS 15004 86020 PROCESS不支持的检测属性，例如FR，有自己独立的处理函数
# MERR_ASF_EX_INVALID_IMAGE_INFO 15005 86021 无效的输入图像
# MERR_ASF_EX_INVALID_FACE_INFO 15006 86022 无效的脸部信息
# MERR_ASF_ACTIVATION_FAIL 16001 90113 SDK激活失败,请打开读写权限
# MERR_ASF_ALREADY_ACTIVATED 16002 90114 SDK已激活
# MERR_ASF_NOT_ACTIVATED 16003 90115 SDK未激活
# MERR_ASF_SCALE_NOT_SUPPORT 16004 90116 detectFaceScaleVal不支持
# MERR_ASF_VERION_MISMATCH 16005 90117 SDK版本不匹配
# MERR_ASF_DEVICE_MISMATCH 16006 90118 设备不匹配
# MERR_ASF_UNIQUE_IDENTIFIER_MISMATCH 16007 90119 唯一标识不匹配
# MERR_ASF_PARAM_NULL 16008 90120 参数为空
# MERR_ASF_LIVENESS_EXPIRED 16009 90121 活体检测功能已过期
# MERR_ASF_VERSION_NOT_SUPPORT 1600A 90122 版本不支持
# MERR_ASF_SIGN_ERROR 1600B 90123 签名错误
# MERR_ASF_DATABASE_ERROR 1600C 90124 数据库插入错误
# MERR_ASF_UNIQUE_CHECKOUT_FAIL 1600D 90125 唯一标识符校验失败
# MERR_ASF_COLOR_SPACE_NOT_SUPPORT 1600E 90126 颜色空间不支持
# MERR_ASF_IMAGE_WIDTH_HEIGHT_NOT_SUPPORT 1600F 90127 图片宽度或高度不支持
# MERR_ASF_READ_PHONE_STATE_DENIED 16010 90128 android.permission.READ_PHONE_STATE权限被拒绝
# MERR_ASF_ACTIVATION_DATA_DESTROYED 16011 90129 激活数据被破坏,请删除激活文件，重新进行激活
# MERR_ASF_NETWORK_COULDNT_RESOLVE_HOST 17001 94209 无法解析主机地址
# MERR_ASF_NETWORK_COULDNT_CONNECT_SERVER 17002 94210 无法连接服务器
# MERR_ASF_NETWORK_CONNECT_TIMEOUT 17003 94211 网络连接超时
# MERR_ASF_NETWORK_UNKNOWN_ERROR 17004 94212 网络未知错误
# MERR_ASF_ACTIVEKEY_COULDNT_CONNECT_SERVER 18001 98305 无法连接激活码服务器
# MERR_ASF_ACTIVEKEY_SERVER_SYSTEM_ERROR 18002 98306 服务器系统错误
# MERR_ASF_ACTIVEKEY_POST_PARM_ERROR 18003 98307 请求参数错误
# MERR_ASF_ACTIVEKEY_PARM_MISMATCH 18004 98308 激活码正确，且未被使用，但和传入的APPID及APPKEY不匹配
# MERR_ASF_ACTIVEKEY_ACTIVEKEY_ACTIVATED 18005 98309 传入的KEY值虽然正确，但此KEY已经被激活
# MERR_ASF_ACTIVEKEY_ACTIVEKEY_FORMAT_ERROR 18006 98310 KEY格式不对，一般来说是KEY错误或者未传入KEY值
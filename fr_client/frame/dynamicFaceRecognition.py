#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/4/3 15:27

import wx


BACK_IMG = 'E:/PycharmProjects/face_recognition_test/fr_client/icon/back.jpg'
class DynamicFaceRecognition(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, '实时人脸识别', size=(800, 600), pos=(270, 100))
        self.panel = wx.Panel(self)
        # wx.StaticText(self, -1, '用户名', (100, 100), (50, -1))
        self.Center()
        self.img = wx.Image(BACK_IMG, wx.BITMAP_TYPE_ANY).Scale(800, 600)
        self.bmp = wx.StaticBitmap(self.panel, -1, wx.Bitmap(self.img))


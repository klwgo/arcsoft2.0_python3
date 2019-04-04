#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/4/3 15:27

import wx

class DynamicFaceRecognition(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, '实时人脸识别', size=(800, 600), pos=(270, 100))
        wx.StaticText(self, -1, '用户名', (100, 100), (50, -1))

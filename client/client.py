#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/4/3 14:18

# 客户端
import wx
import win32api
import sys

APP_TITLE = u'人脸识别系统'
APP_ICON = 'E:/PycharmProjects/face_recognition_test/client/icon/face.ico'
BACK_IMG = 'E:/PycharmProjects/face_recognition_test/client/icon/back.jpg'
class mainFrame(wx.Frame):
    '''程序主窗口类，继承自wx.Frame'''

    def __init__(self, parent):
        '''构造函数'''

        wx.Frame.__init__(self, parent, -1, APP_TITLE)
        to_bmp_image = wx.Image(BACK_IMG, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))
        self.SetBackgroundColour('white')
        self.SetSize((400, 300))
        self.SetMaxSize((400, 300))
        self.Center()
        font = wx.Font(30, wx.DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, 'Monaco')
        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "windows_exe":
            exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
            icon = wx.Icon(exeName, wx.BITMAP_TYPE_ICO)
        else :
            icon = wx.Icon(APP_ICON, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        self.faceDatabaseButton = wx.Button(self.bitmap, -1, u'系统人脸库', size=(100, 40))
        self.staticFaceRecognitionButton = wx.Button(self.bitmap, -1, u'静态人脸识别', size=(100, 40))
        self.dynamicFaceRecognitionButton = wx.Button(self.bitmap,  -1, u'实时人脸识别', size=(100, 40))
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.faceDatabaseButton, 0, wx.ALIGN_CENTER|wx.ALL, 30)
        sizer.Add(self.staticFaceRecognitionButton, 0, wx.ALIGN_CENTER|wx.ALL, 0)
        sizer.Add(self.dynamicFaceRecognitionButton, 0, wx.ALIGN_CENTER|wx.ALL, 30)

        self.dynamicFaceRecognitionButton.Bind(wx.EVT_BUTTON, self.OnDFRB)

        self.SetAutoLayout(True)
        self.SetSizer(sizer)
        self.Layout()


    def OnFDB(self, event):
        pass

    def OnSFRB(self, event):
        pass

    def OnDFRB(self, event):
        self.Show(False)
        self.frame = dynamicFaceRecognition.DynamicFaceRecognition(None)
        self.frame.Show(True)



class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame(None)
        self.Frame.Show()
        return True

def case4():
    app = mainApp()
    app.MainLoop()

case4()

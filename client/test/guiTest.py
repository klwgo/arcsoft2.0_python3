#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/4/3 9:20

# 测试wxpython
import wx
import win32api
import sys, os

def case1():
    app = wx.App()
    frame = wx.Frame(None, -1, "Hello, World!")
    frame.Show(True)
    app.MainLoop()

APP_TITLE = u'基本框架'
APP_ICON = 'E:/PycharmProjects/face_recognition_test/client/test/test.ico'
class mainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, APP_TITLE, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        # 默认style是下列项的组合：wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN

        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.SetSize((800, 600))
        self.Center()

        # # 以下代码处理图标
        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "windows_exe":
            exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
            icon = wx.Icon(exeName, wx.BITMAP_TYPE_ICO)
        else:
            icon = wx.Icon(APP_ICON, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        # 以下可以添加各类控件
        wx.StaticText(self, -1, u'第一行输入框：', pos=(40, 50), size=(100, -1), style=wx.ALIGN_RIGHT)
        wx.StaticText(self, -1, u'第二行输入框：', pos=(40, 80), size=(100, -1), style=wx.ALIGN_RIGHT)
        self.tip = wx.StaticText(self, -1, u'www', pos=(145, 110), size=(150, -1), style=wx.ST_NO_AUTORESIZE)

        self.tc1 = wx.TextCtrl(self, -1, '', pos=(145, 50), size=(150, -1), name='TC01', style=wx.TE_CENTER)
        self.tc2 = wx.TextCtrl(self, -1, '', pos=(145, 80), size=(150, -1), name='TC02',
                               style=wx.TE_PASSWORD | wx.ALIGN_RIGHT)

        btn_mea = wx.Button(self, -1, u'鼠标左键事件', pos=(350, 50), size=(100, 35))
        btn_meb = wx.Button(self, -1, u'鼠标所有事件', pos=(350, 80), size=(100, 25))
        btn_close = wx.Button(self, -1, u'关闭窗口', pos=(350, 110), size=(100, 25))

        # 控件事件
        self.tc1.Bind(wx.EVT_TEXT, self.EvtText)
        self.tc2.Bind(wx.EVT_TEXT, self.EvtText)
        self.Bind(wx.EVT_BUTTON, self.OnClose, btn_close)

        # 鼠标事件
        btn_mea.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        btn_mea.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        btn_mea.Bind(wx.EVT_MOUSEWHEEL, self.OnMouseWheel)
        btn_meb.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)

        # 键盘事件
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

        # 系统事件
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_SIZE, self.On_size)
        # self.Bind(wx.EVT_PAINT, self.On_paint)
        # self.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)

    def EvtText(self, evt):
        '''输入框事件函数'''

        obj = evt.GetEventObject()
        objName = obj.GetName()
        text = evt.GetString()

        if objName == 'TC01':
            self.tc2.SetValue(text)
        elif objName == 'TC02':
            self.tc1.SetValue(text)

    def On_size(self, evt):
        '''改变窗口大小事件函数'''

        self.Refresh()
        evt.Skip()  # 体会作用

    def OnClose(self, evt):
        '''关闭窗口事件函数'''

        dlg = wx.MessageDialog(None, u'确定要关闭本窗口？', u'操作提示', wx.YES_NO | wx.ICON_QUESTION)
        if (dlg.ShowModal() == wx.ID_YES):
            self.Destroy()

    def OnLeftDown(self, evt):
        '''左键按下事件函数'''

        self.tip.SetLabel(u'左键按下')

    def OnLeftUp(self, evt):
        '''左键弹起事件函数'''

        self.tip.SetLabel(u'左键弹起')

    def OnMouseWheel(self, evt):
        '''鼠标滚轮事件函数'''

        vector = evt.GetWheelRotation()
        self.tip.SetLabel(str(vector))

    def OnMouse(self, evt):
        '''鼠标事件函数'''

        self.tip.SetLabel(str(evt.EventType))

    def OnKeyDown(self, evt):
        '''键盘事件函数'''

        key = evt.GetKeyCode()
        self.tip.SetLabel(str(key))


class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame()
        self.Frame.Show()
        return True

def case2():
    app = mainApp(redirect=True, filename="debug.txt")
    app.MainLoop()



APP_TITLE = u'菜单、工具栏、状态栏'
APP_ICON = 'E:/PycharmProjects/face_recognition_test/client/test/test.ico'

class mainFrame(wx.Frame):
    '''程序主窗口类，继承自wx.Frame'''

    id_open = wx.NewId()
    id_save = wx.NewId()
    id_quit = wx.NewId()

    id_help = wx.NewId()
    id_about = wx.NewId()

    def __init__(self, parent):
        '''构造函数'''

        wx.Frame.__init__(self, parent, -1, APP_TITLE)
        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.SetSize((800, 600))
        self.Center()

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "windows_exe":
            exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
            icon = wx.Icon(exeName, wx.BITMAP_TYPE_ICO)
        else :
            icon = wx.Icon(APP_ICON, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        self.Maximize()
        self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE)

        self._CreateMenuBar()         # 菜单栏
        self._CreateToolBar()         # 工具栏
        self._CreateStatusBar()       # 状态栏

    def _CreateMenuBar(self):
        '''创建菜单栏'''

        self.mb = wx.MenuBar()

        # 文件菜单
        m = wx.Menu()
        m.Append(self.id_open, u"打开文件")
        m.Append(self.id_save, u"保存文件")
        m.AppendSeparator()
        m.Append(self.id_quit, u"退出系统")
        self.mb.Append(m, u"文件")

        self.Bind(wx.EVT_MENU, self.OnOpen, id=self.id_open)
        self.Bind(wx.EVT_MENU, self.OnSave, id=self.id_save)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=self.id_quit)

        # 帮助菜单
        m = wx.Menu()
        m.Append(self.id_help, u"帮助主题")
        m.Append(self.id_about, u"关于...")
        self.mb.Append(m, u"帮助")

        self.Bind(wx.EVT_MENU, self.OnHelp,id=self.id_help)
        self.Bind(wx.EVT_MENU, self.OnAbout,id=self.id_about)

        self.SetMenuBar(self.mb)

    def _CreateToolBar(self):
        '''创建工具栏'''

        bmp_open = wx.Bitmap('open.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        bmp_save = wx.Bitmap('save.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        bmp_help = wx.Bitmap('help.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片
        bmp_about = wx.Bitmap('about.png', wx.BITMAP_TYPE_ANY) # 请自备按钮图片

        self.tb = wx.ToolBar(self)
        self.tb.SetToolBitmapSize((16,16))

        self.tb.AddLabelTool(self.id_open, u'打开文件', bmp_open, shortHelp=u'打开', longHelp=u'打开文件')
        self.tb.AddLabelTool(self.id_save, u'保存文件', bmp_save, shortHelp=u'保存', longHelp=u'保存文件')
        self.tb.AddSeparator()
        self.tb.AddLabelTool(self.id_help, u'帮助', bmp_help, shortHelp=u'帮助', longHelp=u'帮助')
        self.tb.AddLabelTool(self.id_about, u'关于', bmp_about, shortHelp=u'关于', longHelp=u'关于...')

        #self.Bind(wx.EVT_TOOL_RCLICKED, self.OnOpen, id=self.id_open)

        self.tb.Realize()

    def _CreateStatusBar(self):
        '''创建状态栏'''

        self.sb = self.CreateStatusBar()
        self.sb.SetFieldsCount(3)
        self.sb.SetStatusWidths([-2, -1, -1])
        self.sb.SetStatusStyles([wx.SB_RAISED, wx.SB_RAISED, wx.SB_RAISED])

        self.sb.SetStatusText(u'状态信息0', 0)
        self.sb.SetStatusText(u'', 1)
        self.sb.SetStatusText(u'状态信息2', 2)

    def OnOpen(self, evt):
        '''打开文件'''

        self.sb.SetStatusText(u'打开文件', 1)

    def OnSave(self, evt):
        '''保存文件'''

        self.sb.SetStatusText(u'保存文件', 1)

    def OnQuit(self, evt):
        '''退出系统'''

        self.sb.SetStatusText(u'退出系统', 1)
        self.Destroy()

    def OnHelp(self, evt):
        '''帮助'''

        self.sb.SetStatusText(u'帮助', 1)

    def OnAbout(self, evt):
        '''关于'''

        self.sb.SetStatusText(u'关于', 1)

class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame(None)
        self.Frame.Show()
        return True

def case3():
    app = mainApp(redirect=True, filename="debug.txt")
    app.MainLoop()

# case3()
class mainFrame(wx.Frame):
    '''程序主窗口类，继承自wx.Frame'''

    def __init__(self, parent):
        '''构造函数'''

        wx.Frame.__init__(self, parent, -1, APP_TITLE)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.SetSize((800, 600))
        self.Center()

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "windows_exe":
            exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
            icon = wx.Icon(exeName, wx.BITMAP_TYPE_ICO)
        else :
            icon = wx.Icon(APP_ICON, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        preview = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        preview.SetBackgroundColour(wx.Colour(0, 0, 0))
        btn_capture = wx.Button(self, -1, u'拍照', size=(100, -1))
        btn_up = wx.Button(self, -1, u'↑', size=(30, 30))
        btn_down = wx.Button(self, -1, u'↓', size=(30, 30))
        btn_left = wx.Button(self, -1, u'←', size=(30, 30))
        btn_right = wx.Button(self, -1, u'→', size=(30, 30))
        tc = wx.TextCtrl(self, -1, '', style=wx.TE_MULTILINE)

        sizer_arrow_mid = wx.BoxSizer()
        sizer_arrow_mid.Add(btn_left, 0, wx.RIGHT, 16)
        sizer_arrow_mid.Add(btn_right, 0, wx.LEFT, 16)

        #sizer_arrow = wx.BoxSizer(wx.VERTICAL)
        sizer_arrow = wx.StaticBoxSizer(wx.StaticBox(self, -1, u'方向键'), wx.VERTICAL)
        sizer_arrow.Add(btn_up, 0, wx.ALIGN_CENTER|wx.ALL, 0)
        sizer_arrow.Add(sizer_arrow_mid, 0, wx.TOP|wx.BOTTOM, 1)
        sizer_arrow.Add(btn_down, 0, wx.ALIGN_CENTER|wx.ALL, 0)

        sizer_right = wx.BoxSizer(wx.VERTICAL)
        sizer_right.Add(btn_capture, 0, wx.ALL, 20)
        sizer_right.Add(sizer_arrow, 0, wx.ALIGN_CENTER|wx.ALL, 0)
        sizer_right.Add(tc, 1, wx.ALL, 10)

        sizer_max = wx.BoxSizer()
        sizer_max.Add(preview, 1, wx.EXPAND|wx.LEFT|wx.TOP|wx.BOTTOM, 5)
        sizer_max.Add(sizer_right, 0, wx.EXPAND|wx.ALL, 0)

        self.SetAutoLayout(True)
        self.SetSizer(sizer_max)
        self.Layout()

class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame(None)
        self.Frame.Show()
        return True

def case4():
    app = mainApp()
    app.MainLoop()

# case4()
import wx.lib.agw.aui as aui
class mainFrame(wx.Frame):
    '''程序主窗口类，继承自wx.Frame'''

    id_open = wx.NewId()
    id_save = wx.NewId()
    id_quit = wx.NewId()

    id_help = wx.NewId()
    id_about = wx.NewId()

    def __init__(self, parent):
        '''构造函数'''

        wx.Frame.__init__(self, parent, -1, APP_TITLE)
        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.SetSize((800, 600))
        self.Center()

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "windows_exe":
            exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
            icon = wx.Icon(exeName, wx.BITMAP_TYPE_ICO)
        else :
            icon = wx.Icon(APP_ICON, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        self.tb1 = self._CreateToolBar()
        self.tb2 = self._CreateToolBar()
        self.tbv = self._CreateToolBar('V')

        p_left = wx.Panel(self, -1)
        p_center0 = wx.Panel(self, -1)
        p_center1 = wx.Panel(self, -1)
        p_bottom = wx.Panel(self, -1)

        btn = wx.Button(p_left, -1, u'切换', pos=(30,200), size=(100, -1))
        btn.Bind(wx.EVT_BUTTON, self.OnSwitch)

        text0 = wx.StaticText(p_center0, -1, u'我是第1页', pos=(40, 100), size=(200, -1), style=wx.ALIGN_LEFT)
        text1 = wx.StaticText(p_center1, -1, u'我是第2页', pos=(40, 100), size=(200, -1), style=wx.ALIGN_LEFT)

        self._mgr = aui.AuiManager()
        self._mgr.SetManagedWindow(self)

        self._mgr.AddPane(self.tb1,
            aui.AuiPaneInfo().Name("ToolBar1").Caption(u"工具条").ToolbarPane().Top().Row(0).Position(0).Floatable(False)
        )
        self._mgr.AddPane(self.tb2,
            aui.AuiPaneInfo().Name("ToolBar2").Caption(u"工具条").ToolbarPane().Top().Row(0).Position(1).Floatable(True)
        )
        self._mgr.AddPane(self.tbv,
            aui.AuiPaneInfo().Name("ToolBarV").Caption(u"工具条").ToolbarPane().Right().Floatable(True)
        )

        self._mgr.AddPane(p_left,
            aui.AuiPaneInfo().Name("LeftPanel").Left().Layer(1).MinSize((200,-1)).Caption(u"操作区").MinimizeButton(True).MaximizeButton(True).CloseButton(True)
        )

        self._mgr.AddPane(p_center0,
            aui.AuiPaneInfo().Name("CenterPanel0").CenterPane().Show()
        )

        self._mgr.AddPane(p_center1,
            aui.AuiPaneInfo().Name("CenterPanel1").CenterPane().Hide()
        )

        self._mgr.AddPane(p_bottom,
            aui.AuiPaneInfo().Name("BottomPanel").Bottom().MinSize((-1,100)).Caption(u"消息区").CaptionVisible(False).Resizable(True)
        )

        self._mgr.Update()

    def _CreateToolBar(self, d='H'):
        '''创建工具栏'''

        bmp_open = wx.Bitmap('open.png', wx.BITMAP_TYPE_ANY)
        bmp_save = wx.Bitmap('save.png', wx.BITMAP_TYPE_ANY)
        bmp_help = wx.Bitmap('help.png', wx.BITMAP_TYPE_ANY)
        bmp_about = wx.Bitmap('about.png', wx.BITMAP_TYPE_ANY)

        if d.upper() in ['V', 'VERTICAL']:
            tb = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize, agwStyle=aui.AUI_TB_TEXT|aui.AUI_TB_VERTICAL)
        else:
            tb = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize, agwStyle=aui.AUI_TB_TEXT)
        tb.SetToolBitmapSize(wx.Size(16, 16))

        tb.AddSimpleTool(self.id_open, u'打开', bmp_open, u'打开文件')
        tb.AddSimpleTool(self.id_save, u'保存', bmp_save, u'保存文件')
        tb.AddSeparator()
        tb.AddSimpleTool(self.id_help, u'帮助', bmp_help, u'帮助')
        tb.AddSimpleTool(self.id_about, u'关于', bmp_about, u'关于')

        tb.Realize()
        return tb

    def OnSwitch(self, evt):
        '''切换信息显示窗口'''

        p0 = self._mgr.GetPane('CenterPanel0')
        p1 = self._mgr.GetPane('CenterPanel1')

        p0.Show(not p0.IsShown())
        p1.Show(not p1.IsShown())

        self._mgr.Update()

class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame(None)
        self.Frame.Show()
        return True

def case5():
    app = mainApp()
    app.MainLoop()
# case5()

import sys, os, time
import threading
class mainFrame(wx.Frame):
    '''程序主窗口类，继承自wx.Frame'''

    def __init__(self, parent):
        '''构造函数'''

        wx.Frame.__init__(self, parent, -1, APP_TITLE)
        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.SetSize((320, 300))
        self.Center()

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "windows_exe":
            exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
            icon = wx.Icon(exeName, wx.BITMAP_TYPE_ICO)
        else :
            icon = wx.Icon(APP_ICON, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        #font = wx.Font(24, wx.DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, 'Comic Sans MS')
        font = wx.Font(30, wx.DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, 'Monaco')

        self.clock = wx.StaticText(self, -1, u'08:00:00', pos=(50,50), size=(200,50), style=wx.TE_CENTER|wx.SUNKEN_BORDER)
        self.clock.SetForegroundColour(wx.Colour(0, 224, 32))
        self.clock.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.clock.SetFont(font)

        self.stopwatch = wx.StaticText(self, -1, u'0:00:00.0', pos=(50,150), size=(200,50), style=wx.TE_CENTER|wx.SUNKEN_BORDER)
        self.stopwatch.SetForegroundColour(wx.Colour(0, 224, 32))
        self.stopwatch.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.stopwatch.SetFont(font)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.timer.Start(50)

        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

        self.sec_last = None
        self.is_start = False
        self.t_start = None

        thread_sw = threading.Thread(target=self.StopWatchThread)
        thread_sw.setDaemon(True)
        thread_sw.start()

    def OnTimer(self, evt):
        '''定时器函数'''

        t = time.localtime()
        if t.tm_sec != self.sec_last:
            self.clock.SetLabel('%02d:%02d:%02d'%(t.tm_hour, t.tm_min, t.tm_sec))
            self.sec_last = t.tm_sec

    def OnKeyDown(self, evt):
        '''键盘事件函数'''

        if evt.GetKeyCode() == wx.WXK_SPACE:
            self.is_start = not self.is_start
            self.t_start= time.time()
        elif evt.GetKeyCode() == wx.WXK_ESCAPE:
            self.is_start = False
            self.stopwatch.SetLabel('0:00:00.0')

    def StopWatchThread(self):
        '''线程函数'''

        while True:
            if self.is_start:
                n = int(10*(time.time() - self.t_start))
                deci = n%10
                ss = int(n/10)%60
                mm = int(n/600)%60
                hh = int(n/36000)
                wx.CallAfter(self.stopwatch.SetLabel, '%d:%02d:%02d.%d'%(hh, mm, ss, deci))
            time.sleep(0.02)

class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame(None)
        self.Frame.Show()
        return True

def case6():
    app = mainApp()
    app.MainLoop()
case6()
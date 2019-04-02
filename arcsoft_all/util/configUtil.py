#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/4/2 9:04

import configparser
import os


config = configparser.ConfigParser()
# 初始化
def init():
    config.read(os.path.join(os.path.dirname((os.path.dirname(__file__))), 'conf/config.ini'))

# 获取值
def getValue(type, key):
    init()
    return config.get(type, key)
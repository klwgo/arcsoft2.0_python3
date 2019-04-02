#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/4/1 16:40
import configparser
import os

config = configparser.ConfigParser()
# config.read('E:/PycharmProjects/face_recognition_test/arcsoft_all/conf/config.ini')
config.read(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'conf/config.ini'))
print(config.get('arcsoft', 'APP_ID'))
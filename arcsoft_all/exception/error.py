#!/usr/bin/env python
#! -*- coding:utf-8 -*-
#!@Author: faple
#!@Time: 2019/4/2 9:25

class BaseException(Exception):

    def __init__(self, errorinfo):
        self.error = errorinfo

    def __str__(self):
        return self.error
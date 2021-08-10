#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/8/10


"""
监听文件输入
"""
def tail(filename):
    f = open(filename, encoding="utf-8")
    while True:
        line = f.readline()
        if line.strip():
            yield line.strip()

ret = tail("test.txt")
for i in ret:
    if 'python' in i:
        print("***",i)
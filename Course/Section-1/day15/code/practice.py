#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/8/16

"""
3.处理文件，用户指定要查找的文件和内容，将文件中包含要查找内容的每一行都输出到屏幕.
"""
# def checkFile(filename):
#     with open(filename, encoding="utf-8") as f:
#         for i in f:
#             if "约定" in i:
#                 yield i
# for line in checkFile("test.txt"):
#     print(line.strip())

"""
# 4.写生成器，从文件中读取内容，在每一次读取到的内容之前加上‘***’之后再返回给用户。
"""

# def findText(filename):
#     with open(filename, encoding="utf-8") as f:
#         for line in f:
#             yield '***'+line
# for line in findText("test.txt"):
#     print(line.strip())

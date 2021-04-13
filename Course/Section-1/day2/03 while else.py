#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/4/13

"""
while 条件:
    循环体
else:
    正常执行完了(遇到break退出循环就不会执行else)
"""
count = 0
while count <= 5:
    count += 1
    if count == 3:
        break
    print("Loop", count)

else:
    print("循环正常执行完啦")
print("-----out of while loop ------")
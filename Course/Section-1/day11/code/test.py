#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/7/31

# --------------------------------------------------------------------------------------
# 1，写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)
# def max_min(*args):
#     num_dic = {"max": max(args), "min": min(args)}
#     return num_dic
# ret = max_min(2,5,7,8,4)
# print(ret)

# --------------------------------------------------------------------------------------
# 2，写函数，传入一个参数n，返回n的阶乘
#   例如:cal(7) 计算7654321
# def cal(n):
#     total = 1
#     for i in range(1, n+1):
#         total *= i
#     return total
# print(cal(7))

# --------------------------------------------------------------------------------------
#3，写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组

#例如：[(‘红桃’，2),(‘梅花’，2), …(‘黑桃’，‘A’)]


#4，有如下函数:

# def wrapper():
#     def inner():
#         print(666)
# wrapper()
# 你
#         print(666)
#     return inner()
# wrapper()可以任意添加代码,用两种或以上的方法,执行inner函数.
# #
# # # def wrapper():
# # #     def inner():






# 5，相关面试题（先从纸上写好答案，然后在运行）：
#
# 5.1，有函数定义如下：
#

# # 请分别写出下列标号代码的输出结果，如果出错请写出Error。
# print(calc(1,2,3,4,5)) # 2
# print(calc(1,2)) # error
# print(calc(e=4,c=5,a=2,b=3)) #
# print(calc(1,2,3)) #
# print(calc(1,2,3,e=4)) #
# print(calc(1,2,3,d=5,4)) # error
# 5.2，下面代码打印的结果分别是 list1= ,list2= ,list3= .
#

# 5.3，写代码完成99乘法表.(升级题)
#
# * 1 = 1
# * 1 = 2 2 * 2 = 4
# * 1 = 3 3 * 2 = 6 3 * 3 = 9
# ......
# * 1 = 9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81



#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/7/29

# ########################################################################
# 1, 继续整理函数相关知识点，写博客。

##########################################################################
# 2, 写函数，接收n个数字，求这些参数数字的和。（动态传参）
# def num_sum(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# li1 = [11, 2, 34, 553, 32, 42]
# print(num_sum(*li1))

#############################################################################
# ### 3,读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？

# a=10
# b=20
# def test5(a,b):
#          print(a,b)
# c = test5(b,a)
# print(c) # a=20 b=10 c = None

#############################################################################
# ### 4,读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# a = 10
# b = 20
# def test5(a, b):
#     a=3
#     b=5
#     print(a,b)
# c = test5(b,a)
# print(c) #a=3 b=5 c None


# ############################################################################
"""5,写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等),将每个实参的每个元素依次添加到函数的动态参数args里面.
     例如:传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)"""
# li1 = [1, 2, 3]
# tu1 = (22, 33)
# set1 = {11, 44}
# lis1 = "abc"
# def format_args(*args):
#     print(args)
#
# format_args(*li1, *tu1, *lis1)


# ############################################################################
# ### 6,写函数,传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs里面.
# 例如 传入函数两个参数{‘name’:’alex’} {‘age’:1000}最终kwargs为{‘name’:’alex’ ,‘age’:1000}

# dic1 = {"name": "alex"}
# dic2 = {"age": 1000}
# def format_dict(**kwargs):
#     print(kwargs)
# format_dict(**dic1, **dic2)

# ############################################################################
#  7, 下面代码成立么?如果不成立为什么报错?怎么解决?
# 7.1

# a = 2
# def wrapper():
#     print(a)  # 取外部变量a
# wrapper()

#
# ### 7.2
# a = 2
# def wrapper():
#     global a  # 增加全局申明才能改
#     a += 1
#     print(a)
# wrapper()


# ### 7.3

# def wrapper():
#     a = 1
#     def inner():
#         print(a)  # 取外部的a
#     inner()
# wrapper()

# ### 7.4

# def wrapper():
#     a = 1
#     def inner():
#         nonlocal a  # 增加部分，指定a使用上一次的a，且只能使用局部变量的值
#         a += 1
#         print(a)
#     inner()
# wrapper()

# ############################################################################
# 8，写函数,接收两个数字参数,将较小的数字返回.
# ############################################################################

# def min_num(a,b):
#     if a > b:
#         return b
#     else:
#         return a
#
# ref = min_num(22,1)
# print(ref)

# ############################################################################
# ### 9，写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以’_’相连接,形成新的字符串,并返回.
# 例如 传入的可迭代对象为[1,'老男孩','武sir']返回的结果为’1_老男孩_武sir’

# li1 = [1, '老男孩', '武sir']
# def format_str(*args):
#     li = []
#     for i in range(len(args)):
#         if type(args[i]) != str:
#             li.append(str(args[i]))
#         else:
#             li.append(args[i])
#     return "_".join(li)
#
# ref = format_str(*li1)
# print(ref)

# li1 = ["11", '老男孩', '武sir']
# str1 = "_".join(li1)
# print(str1)

# ############################################################################
# ### 10,写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 例如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)
# def min_max(*args):
#     dic1 = {}
#     dic1["max"] = max(args)
#     dic1["min"] = min(args)
#     return dic1
# ret = min_max(2,5,7,8,4)
# print(ret)

# ############################################################################
# ### 11,写函数，传入一个参数n，返回n的阶乘
# 例如:cal(7)  计算7*6*5*4*3*2*1
# def cal(n):
#     total = 1
#     for i in range(1, n+1):
#         print(i)
#         total *= i
#     return total
# print(cal(7))


# ############################################################################
# ### 12写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组（升级题）
# 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]
# def card():
#     temp_list = []
#     card = []
#     for i in range(2, 11):
#         temp_list.append(i)
#         temp_list.extend(["J", "Q", "K", "A"])
#     for i in temp_list:
#         for card_type in ["黑桃", "红桃", "方块", "草花"]:
#             a = (card_type, i)
#             card.append(a)
#     return card
#
# res = card()
# print(res)、

# def card():
#     temp_list = []
#     card_list = []
#     for i in range(2,11):
#         temp_list.append(i)
#         temp_list.extend(["J", "Q", "K", "A"])
#     for i in temp_list:
#         for card_type in ["黑桃", "红桃", "方块", "草花"]:
#             a = (card_type, i)
#             card_list.append(a)
#     return card_list
# ret = card()
# print(ret)


# 13 有如下函数:
# ```python
# def wrapper():
#         def inner():
#             print(666)
#     wrapper()
# ```
#
# 你可以任意添加代码,用两种或以上的方法,执行inner函数.

# 方法一
# def wrapper():
#     def inner():
#         print(666)
#     inner()
# wrapper()

# 方法二

# def wrapper():
#     def inner():
#         print(666)
#     return inner
# ret = wrapper()
# ret()
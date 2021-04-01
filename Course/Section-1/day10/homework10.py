#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: 2018/12/24
#
# 1, 继续整理函数相关知识点，写博客。
#
# 2, 写函数，接收n个数字，求这些参数数字的和。（动态传参）

def cal(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum
list1 = [1,2,55,33,22,34,123,442,332,1124,23,2]
print(cal(*list1))
#
# ### 3,读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？

# a=10
# b=20
# def test5(a,b):
#          print(a,b)
# c = test5(b,a)
# print(c) # a=20 b=10 c=None

#
# ### 4,读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？

# a=10
# b=20
# def test5(a,b):
#     a=3
#     b=5
#     print(a,b)
# c = test5(b,a)
# print(c) # a=3 b=5 c=None

"""5,写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等),将每个实参的每个元素依次添加到函数的动态参数args里面.
     例如:传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)"""
def joindata(*args):
    new_args = []
    for i in range(len(args)):
        if type(i) == set:
            i = list(i)
            for j in range(len(i)):
               new_args.append(i[j])
        else:
            for j in range(len(i)):
               new_args.append(i[j])
list2 = ['abad',{1,2,3,4},(1,'a','cd'),['a','b',1,'ab']]
print(joindata(*list2))

# ### 6,写函数,传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs里面.
# 例如 传入函数两个参数{‘name’:’alex’} {‘age’:1000}最终kwargs为{‘name’:’alex’ ,‘age’:1000}
# ### ### 7, 下面代码成立么?如果不成立为什么报错?怎么解决?
# ### 7.1
# ```python
#     a = 2
#     def wrapper():
#             print(a)
#     wrapper()
# ```
#
# ### 7.2
# ```python
#     a = 2
#     def wrapper():
#             a += 1
#         print(a)
#     wrapper()
# ```
# ### 7.3
# ```python
# def wrapper():
#         a = 1
#         def inner():
#             print(a)
#         inner()
#     wrapper()
# ```
# ### 7.4
# ```python
# def wrapper():
#         a = 1
#         def inner():
#             a += 1
#             print(a)
#         inner()
#     wrapper()
# ```
#
# ### 8，写函数,接收两个数字参数,将较小的数字返回.
#
# ### 9，写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以’_’相连接,形成新的字符串,并返回.
# 例如 传入的可迭代对象为[1,'老男孩','武sir']返回的结果为’1_老男孩_武sir’
#
# ### 10,写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 例如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)
#
# ### 11,写函数，传入一个参数n，返回n的阶乘
# 例如:cal(7)  计算7*6*5*4*3*2*1
#
# ### 12写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组（升级题）
# 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]
# 有如下函数:
# ```python
# def wrapper():
#         def inner():
#             print(666)
#     wrapper()
# ```
#
# 你可以任意添加代码,用两种或以上的方法,执行inner函数.


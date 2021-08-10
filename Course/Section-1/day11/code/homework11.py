#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: 2018/12/23

# 1，写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}

#如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)
def min_max(*args):
    dict1 = {}
    for i in range(len(args)):
        if  i == 1:
            dict1["max"] = max(args[i],args[i-1])
            dict1["min"] = min(args[i],args[i-1])
        elif i > 0:
            dict1["max"] = max(args[i],dict1["max"])
            dict1["min"] = min(args[i],dict1["min"])
    return dict1
list1 =[1,2,13,33,44,22,-1,-200,+2000,-222,22,55]
print(min_max(*list1))

# 2，写函数，传入一个参数n，返回n的阶乘

#例如:cal(7) 计算7654321

def cal(num):
    """计算自然数的阶乘"""
    sum = 1
    if num == 0 and num == 1:
        return 1
    elif num >1:
        for i in range(2,num+1):
            sum *=i
        return sum

print(cal(8))


#3，写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组

#例如：[(‘红桃’，2),(‘梅花’，2), …(‘黑桃’，‘A’)]

def card():
    list1 = [2,3,4,5,6,7,8,9,10,'A','J','Q','K']
    list2 = ['黑桃','红桃',"梅花","方块"]
    card1 = []
    for i in list2:
        for j in list1:
            a = (i,j)
            card1.append(a)
    return card1
print(card())

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
import time
def wrapper(func):
    def inner(*args,**kwargs):
        start = time.time()
        ret=func(*args,**kwargs)
        end = time.time()
        return ret
    return inner


@wrapper
def func():
    time.sleep(1)
    print("In the func")
    return "In the func"
print(func())


# 5，相关面试题（先从纸上写好答案，然后在运行）：
#
# 5.1，有函数定义如下：
#
def calc(a,b,c,d=1,e=2):
    return (a+b)*(c-d)+e
# # 请分别写出下列标号代码的输出结果，如果出错请写出Error。
# print(calc(1,2,3,4,5)) # 2
# print(calc(1,2)) # error
# print(calc(e=4,c=5,a=2,b=3)) #
# print(calc(1,2,3)) #
# print(calc(1,2,3,e=4)) #
# print(calc(1,2,3,d=5,4)) # error
# 5.2，下面代码打印的结果分别是 list1= ,list2= ,list3= .
#
def extendList(val,list=[]):
    list.append(val)
    return list
list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')
print('list1=%s'%list1) # 10,'a'
print('list2=%s'%list2) #123
print('list3=%s'%list3) # 10,'a'
# 5.3，写代码完成99乘法表.(升级题)
#
# * 1 = 1
# * 1 = 2 2 * 2 = 4
# * 1 = 3 3 * 2 = 6 3 * 3 = 9
# ......
# * 1 = 9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81


def multiplacation():
    """乘法口诀表"""
    list =[1,2,3,4,5,6,7,8,9]
    for  i in  range(1,10):
        for j in range(1,10):
            if j <= i:
                print("%s*%s=%s"%(i,j,i*j),end=' ')
        print( )
multiplacation()
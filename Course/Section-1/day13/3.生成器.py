#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/8/10

"""
生成器函数
"""
# def generator():
#     print(1)
#     return 'a'
#
# ret = generator()
# print(ret)

"""
1, 只要含有yield关键字的函数都是生成器函数(定义)
2, yield不能和return共用
3, yield需要写在函数内
"""

# def generator():
#     print(1)
#     yield 'a'
# ret = generator()
# print(ret)
# print(ret.__next__())

"""
生成器函数 ： 执行之后会得到一个生成器作为返回值
return 结束函数，yield不会结束函数。
next 一个个循环，for全部循环。
"""

# def generator():
#     print(1)
#     yield 'a'
#     print(2)
#     yield 'b'
#     yield 'c'
# g = generator()
# # for i in g:
# #     print(i)
# ret = g.__next__()
# print(ret)
# ret = g.__next__()
# print(ret)
#
# ret = g.__next__()
# print(ret)


"""
制造两百个哇哈哈
"""
# def wahaha():
#     for i in range(2000000):
#         yield '娃哈哈%s'%i
# g = wahaha()
# g1 = wahaha()
# print(g.__next__())
# print(g1.__next__())


def whaha():
    for i in range(200):
        yield "wahaha%s" % i


g = whaha()
count = 0
for i in g:
    count += 1
    print(i)
    if count > 50:
        break
# print('*******',g.__next__())
# print('*******',g.__next__())
# g = wahaha()
# count = 0
# for i in g:
#     count +=1
#     print(i)
#     if count > 50:
#         break
# # print('*******',g.__next__())

# for i in g:
#     count +=1
#     print(i)
#     if count > 100:
#         break

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/7/27


# 2，写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def check(*args):
#     lis1 = []
#     for i in range(len(args)):
#         if i % 2 != 0:
#             lis1.append(args[i])
#     return lis1
# lis = [11, 22, 44, 55, 43, 32, 43, 343, 34, 32, 11]
# tu1 = (11, 22, 44, 55, 43, 32, 43, 343, 34, 32, 11)
# print(check(*lis))
# print(check(*tu1))


# 3，写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def test_len(*args):
#     if len(args) > 5:
#         return True
#     else:
#         return False
# print(test_len(*"aaadfdgd"))
# print(test_len(*[11, 22, 44, 55, 43, 32, 43, 343, 34, 32, 11]))
# print(test_len(*(34, 32, 11)))

# 4，写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# li1 = [11, 22, 44, 55, 43, 32, 43, 343, 34, 32, 11]
# li2 = [11, 22]
# def test_len(*args):
#     if len(args) > 2:
#         return args[:2]
#     else:
#         return args
# print(test_len(*li1))
# print(test_len(*li2))

# 5，写函数，计算传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。
# s1 = " sfs1 42ssf  ss 我爱你/*"
# def count_type(*args):
#     total = []
#     num = 0
#     str_num = 0
#     others = 0
#     space_num = args.count(" ")
#     for i in args:
#         if i.isdigit():
#             num += 1
#         if i.isalpha():
#             str_num += 1
#     others = len(args) - num - str_num -space_num
#     total.append(num)
#     total.append(str_num)
#     total.append(space_num)
#     total.append(others)
#     return total
# print(count_type(*s1))

# 6，写函数，接收两个数字参数，返回比较大的那个数字。
# def bigger(a,b):
#     if a -b > 0:
#         return a
#     else:
#         return b
# print(bigger(2,3))
# print(bigger(-1,5))


# 7,写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# info = {"name":"zhaozhao", "age":"23", "sex":"男"}
# def check_dict(**kwargs):
#     info = {}
#     for key,value in kwargs.items():
#         if len(value) > 2:
#             info[key] = value[:2]
#         else:
#             info[key] = value
#     return info
#
# print(check_dict(**info))



"""
8，写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，
此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
"""



"""9，写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这四个内容传入到函数中，
此函数接收到这四个内容，将内容追加到一个student_msg文件中。"""




'''10，对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。'''


'''11，写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（升级题）。'''



'''12，写一个函数完成三次登陆功能：(升级题, 两天做完)
(1)用户的用户名密码从一个文件register中取出。
(2)register文件
(4)登陆成功返回True。包含多个用户名，密码，用户名密码通过 | 隔开，每个人的用户名密码占用文件中一行。
(3)完成三次验证，三次验证不成功则登录失败，登录失败返回False。
'''
'''13，再写一个函数完成注册功能：(升级题, 两天做完)
(1)用户输入用户名密码注册。
(2)注册时要验证（文件regsiter中）用户名是否存在，如果存在则让其重新输入用户名，如果不存在，则注册成功。
(3)注册成功后，将注册成功的用户名，密码写入regsiter文件，并以 | 隔开。
(4)注册成功后，返回True, 否则返回False。
'''
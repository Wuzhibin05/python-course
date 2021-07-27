#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2018/12/20

# 2，写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
l1 = [1,2,'alex',[1,2,3],'wuzb']
def search(l1):
    l2 = []
    for i in range(len(l1)):
        if i % 2 != 0:
            l2.append(l1[i])
    return l2
print(search(l1))


# 3，写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
l3 = 'sga142141'
def len_test(*args):
    if len(args)>5:
        return True
    else:
        return False
print(len_test(*l3))


# 4，写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
l4 = [1,2,'alex',[1,2,3],'wuzb']
def len1(*args):
    l5 = []
    if len(args) > 2:
        l5.append(args[0])
        l5.append(args[1])
        return l5
print(len1(*l4))
# 5，写函数，计算传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。
s = " sfs1 42ssf  ss 我爱你"
def count(*args):
    total = []
    str_num = 0
    num = 0
    others = 0
    space = 0
    space = args.count(" ")
    for i in args:
        if i.isdigit():
            num +=1
        elif i.isalpha():
            str_num += 1
    others = len(args)- space - num - str_num
    total.append(str_num)
    total.append(num)
    total.append(space)
    total.append(others)
    return total
print(count(*s))

# 6，写函数，接收两个数字参数，返回比较大的那个数字。

def bigger(x,y):
    """
    比较两个数的大小，返回大的
    """
    if x > y:
        return x
    else:
        return y

print(bigger(5,y=100))

# 7,写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
def get_values(**kwargs):
    """
    function: truncate the first two values of the dict.
    Returns: list
    """
    lst = []
    for i in kwargs.values():
        if len(i)>2:
            lst.append(i[:2])
    return lst
print(get_values(**dic))

"""
8，写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，
此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
"""
lst1 = [11,22,44,44,12,433,[12421,123]]
def transform(*args):
    """
    transform list to dict
    """
    dic1 = {}
    if len(args) != 0:
        for index, i in enumerate(args):
            dic1[index] = i
    return dic1
print(transform(*lst1))


"""9，写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这四个内容传入到函数中，
此函数接收到这四个内容，将内容追加到一个student_msg文件中。"""

# def format_message(**kwargs):
#
#     with open('student_msg.txt', mode='a+',encoding='utf-8') as f:
#         f.write("开始写入数据 ".center(50,"-")+"\n")
#         f.write("name:%s \n" %kwargs["name"])
#         f.write("sex:%s \n"%kwargs["sex"])
#         f.write("age:%s \n"%kwargs["age"])
#         f.write("education:%s \n"%kwargs["education"])
#
# username = input("Please input your name:")
# sex = input("Please input your sex:")
# age = input("Please input your age:")
# education = input("Please input your education:")
# dic2 = {}
# dic2["name"] = username
# dic2["sex"] = sex
# dic2["age"] = age
# dic2["education"] = education
# print(format_message(**dic2))


'''10，对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。'''
# def format_message(sex = "男",**kwargs):
#     """
#     将用户输入的姓名，性别，年龄和学习追加写入到文件。
#     """
#     with open('student_msg.txt', mode='a+',encoding='utf-8') as f:
#         f.write("开始写入数据 ".center(50,"-")+"\n")
#         f.write("name:%s \n" %kwargs["name"])
#         f.write("sex:%s \n"%sex)
#         f.write("age:%s \n"%kwargs["age"])
#         f.write("education:%s \n"%kwargs["education"])
# while True:
#     print("If you want to quit,please input 'q'or'Q':".center(80,'='))
#     username = input("Please input your name:").strip()
#     if username.upper() == "Q":
#         break
#     sex = input("Please input your sex:").strip()
#     if sex.upper() == "Q":
#         break
#     age = input("Please input your age:").strip()
#     if age.upper() == "Q":
#         break
#     education = input("Please input your education:").strip()
#     if education.upper() == "Q":
#         break
#     dic2 = {}
#     dic2["name"] = username
#     dic2["age"] = age
#     dic2["education"] = education
#     if sex == "女":
#         print(format_message(sex = "女",**dic2))
#     else:
#         print(format_message(**dic2))

'''11，写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（升级题）。'''
import os
def modify_file(file,s):
    new_line = ''
    s2 = input("请输入你要修改后的内容:").strip()
    with open(file, mode='r',encoding='utf-8') as f,open(file+'.bak',mode='w+',encoding = 'utf-8') as f2:
        for line in f:
            if s in line:
                new_line =line.replace(s,s2)
                f2.write(new_line)
                continue
            f2.write(line)
            print(line)
    # 判断文件是否 文件是否存在并替换。
    os.remove(file)
    os.rename(file+".bak",file)
filename = '../student_msg1.txt'
s1= input("请输入你想要修改的内容:").strip()
modify_file(filename,s1)


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
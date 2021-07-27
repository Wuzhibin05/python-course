#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/7/27

# #####################################################################
# 1，有如下文件，a1.txt，里面的内容为：
#
# 老男孩是最好的学校，
# 全心全意为学生服务，
# 只为学生未来，不为牟利。
# 我说的都是真的。哈哈
#
# 分别完成以下的功能：

# a,将原文件全部读出来并打印。
# f = open('a1.txt', mode='r', encoding='utf-8')
# s = f.read()
# print(s)
# f.close()

# b,在原文件后面追加一行内容：信不信由你，反正我信了。
# f = open('a1.txt', mode='a+', encoding='utf-8')
# f.write("\n")
# f.write("信不信由你，反正我信了")

# c,将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我信了。
# with open('a1.txt', mode='r+', encoding='utf-8') as f:
#     f.write("\n信不信由你，反正我信了")
#     for i in f:
#         print(i)

# d,将原文件全部清空，换成下面的内容：
# 每天坚持一点，
# 每天努力一点，
# 每天多思考一点，
# 慢慢你会发现，
# 你的进步越来越大。
# with open('a1.txt', mode='r+', encoding='utf-8') as f:
#     f.truncate()
#     f.write("每天坚持一点，")
#     f.write("\n每天努力一点，")
#     f.write("\n每天多思考一点，")
#     f.write("\n慢慢你会发现，")
#     f.write("\n你的进步越来越大。")

# e,将原文件内容全部读取出来，并在‘我说的都是真的。哈哈’这一行的前面加一行，‘你们就信吧~’然后将更改之后的新内容，写入到一个新文件：a1.txt。
# import os
# check_str = "我说的都是真的。哈哈"
# with open('a1.txt', mode='r', encoding='utf-8') as f1, open('a2.txt', mode='r+', encoding='utf-8') as f2:
#     f2.truncate()
#     for line in f1:
#         if check_str in line:
#             f2.write("你们就信吧~\n")
#         f2.write(line)
# os.remove('a1.txt')
# os.rename('a2.txt', 'a1.txt')

# #####################################################################
# 2，有如下文件，t1.txt,里面的内容为：
#
# 葫芦娃，葫芦娃，
# 一根藤上七个瓜
# 风吹雨打，都不怕，
# 啦啦啦啦。
# 我可以算命，而且算的特别准:
# 上面的内容你肯定是心里默唱出来的，对不对？哈哈
#
# 分别完成下面的功能：
# a,以r+的模式打开原文件，判断原文件是否可读，是否可写。
# with open('a3.txt', mode='r+', encoding='utf-8') as f:
#     print(f.readable())
#     print(f.writable())

# b,以r的模式打开原文件，利用for循环遍历文件句柄。
# with open('a3.txt', mode='r', encoding='utf-8') as f:
#     for line in f:
#         print(line)


# c,以r的模式打开原文件，以readlines()方法读取出来，并循环遍历
# readlines(),并分析b,与c 有什么区别？深入理解文件句柄与 readlines()结果的区别。
# f = open('a3.txt', mode='r', encoding='utf-8')
# s = f.readlines()
# for line in s:
#     print(line)

# d,以r模式读取‘葫芦娃，’前四个字符。
# with open('a3.txt', mode='r', encoding='utf-8') as f:
#     f.seek(0)
#     s = f.read(4)
#     print(s)


# e,以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。


# f,以r模式打开文件，从‘风吹雨打.....’开始读取，一直读到最后。
# check_str = "风吹雨打，都不怕，"



# g,以a+模式打开文件，先追加一行：‘老男孩教育’然后在从最开始将 原内容全部读取出来。
# insert_str = "老男孩教育"




# # h,截取原文件，截取内容：‘葫芦娃，葫芦娃，’
# truncate_str = '葫芦娃，葫芦娃,'



# #####################################################################
# 3，文件a.txt内容：每一行内容分别为商品名字，价钱，个数。
#
# apple 10 3
# tesla 100000 1
# mac 3000 2
# lenovo 30000 3
# chicken 10 3
#
# 通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......]
# 并计算出总价钱。




# #####################################################################
# 将文件中所有的alex都替换成大写的SB（文件的改的操作）。# 4，有如下文件：
#
# alex是老男孩python发起人，创建人。
# alex其实是人妖。
# 谁说alex是sb？
# 你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。
#



# #####################################################################
# 5，文件a1.txt内容(升级题)
#
# name:apple price:10 amount:3 year:2012
# name:tesla price:100000 amount:1 year:2013
# .......
#
# 通过代码，将其构建成这种数据类型：
# [{'name':'apple','price':10,'amount':3},
# {'name':'tesla','price':1000000,'amount':1}......]
# 并计算出总价钱。
# shopping_car = []
# product_dict = {}
# total = 0



# #####################################################################
# 6，文件a1.txt内容(升级题)
#
# 序号     部门      人数      平均年龄      备注
#       python    30         26         单身狗
#       Linux     26         30         没对象
#       运营部     20         24         女生多
# .......
# 通过代码，将其构建成这种数据类型：
# [{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},
# ......]



# #####################################################################
# 7,查看当前文件夹某一文件编码
# import chardet
# path = "D:/Python14/Python_Project/Python18/day8/a1.txt"
# f = open(path,'rb')
# data = f.read()
# print(chardet.detect(data))
# print(f.fileno())

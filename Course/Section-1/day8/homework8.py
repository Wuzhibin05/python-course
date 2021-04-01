#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: 2018/12/20

# 1，有如下文件，a1.txt，里面的内容为：
#
# 老男孩是最好的学校，
# 全心全意为学生服务，
# 只为学生未来，不为牟利。
# 我说的都是真的。哈哈
#
# 分别完成以下的功能：

# a,将原文件全部读出来并打印。
# with open("./a1.txt","r",encoding="utf-8") as f:
#     for line in f:
#         print(line)

# b,在原文件后面追加一行内容：信不信由你，反正我信了。
# with open("./a1.txt","a",encoding="utf-8") as f:
#     f.write("\n信不信由你，反正我信了")


# c,将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我信了。
# f = open('a1.txt',mode='r+',encoding='utf-8')
# f.read()
# f.write("\n信不信由你，反正我信了")

# d,将原文件全部清空，换成下面的内容：
# 每天坚持一点，
# 每天努力一点，
# 每天多思考一点，
# 慢慢你会发现，
# 你的进步越来越大。
# f = open('a1.txt',mode='w',encoding='utf-8')
# f.write("# 每天坚持一点，")
# f.write("\n# 每天努力一点，")
# f.write("\n# 每天坚持一点，")
# f.write("\n# 每天坚持一点，")
# f.write("\n# 每天坚持一点，")

# e,将原文件内容全部读取出来，并在‘我说的都是真的。哈哈’这一行的前面加一行，‘你们就信吧~’然后将更改之后的新内容，写入到一个新文件：a1.txt。
# check_line ="我说的都是真的。哈哈"
# write_line ="你们就信吧"
# with open('a1.txt',mode='r',encoding='utf-8') as old,open('a2.txt',mode='w',encoding='utf-8') as new:
#     for line in old:
#         if check_line in line:
#             new.write(write_line+"\n")
#             new.write(line)
#             continue
#         else:
#             new.write(line)


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
#     # print(f.readline())
#     for line in f:
#         print(line)


# c,以r的模式打开原文件，以readlines()方法读取出来，并循环遍历
# readlines(),并分析b,与c 有什么区别？深入理解文件句柄与 readlines()结果的区别。
# with open('a3.txt', mode='r', encoding='utf-8') as f:
#     # print(f.readline())
#     lines = f.readlines()
#     for line in lines:
#         print(line)

# d,以r模式读取‘葫芦娃，’前四个字符。
# with open('a3.txt', mode='r', encoding='utf-8') as f:
#     f.seek(0)
#     s= f.read(4)
#     print(s)


# e,以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。
# with open('a3.txt', mode='r', encoding='utf-8') as f:
#     s= f.readline().strip()
#     print(s)

# f,以r模式打开文件，从‘风吹雨打.....’开始读取，一直读到最后。
# check_str = "风吹雨打，都不怕，"
# with open('a3.txt', mode='r', encoding='utf-8') as f:
#     n = 0
#     for line in f:
#         if n == 0 :
#             if line.strip().startswith(check_str):
#                 print(line)
#                 n = 1
#                 continue
#         if n == 1:
#             print(line)


# g,以a+模式打开文件，先追加一行：‘老男孩教育’然后在从最开始将 原内容全部读取出来。
# insert_str = "老男孩教育"
# with open('a3.txt', mode='a+', encoding='utf-8') as f:
#     f.write("\n"+insert_str)
#     f.seek(0)
#     for line in f:
#         print(line)



# # h,截取原文件，截取内容：‘葫芦娃，葫芦娃，’
# truncate_str = '葫芦娃，葫芦娃,'
# with open('a3.txt', mode='r+', encoding='utf-8') as f:
#     f.seek(0)
#     f.truncate(24)


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
# shopping_car = []
# product_dict = {}
# total = 0
# with open('a4.txt', mode='r', encoding='utf-8') as f:
#     for line in f:
#         new_line = line.strip().split(" ")
#         product_dict["name"] = new_line[0]
#         product_dict["price"] = new_line[1]
#         product_dict["amount"] = new_line[2]
#         shopping_car.append(product_dict)
#     print(shopping_car)
#
# for i in range(len(shopping_car)):
#     total = total + int(shopping_car[i]["price"])
# print(total)




# 将文件中所有的alex都替换成大写的SB（文件的改的操作）。# 4，有如下文件：
#
# alex是老男孩python发起人，创建人。
# alex其实是人妖。
# 谁说alex是sb？
# 你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。
#
# import os
# replace_str = 'alex'
# with open('a5.txt', mode='r', encoding='utf-8') as old_file ,open('a6.txt',mode='w+', encoding='utf-8') as new_file:
#     for line in old_file:
#         if  replace_str in line:
#             new_line = line.replace(replace_str,"SB")
#             new_file.write(new_line)
#             continue
#         new_file.write(line)
# os.remove('a5.txt')
# os.rename('a6.txt','a5.txt')


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
# with open('a7.txt', mode='r', encoding='utf-8') as f:
#     for line in f:
#         new_line = line.strip().split(" ")
#         name_line =new_line[0].strip().split(":")
#         price_line =new_line[1].strip().split(":")
#         amount_line =new_line[2].strip().split(":")
#         year_line =new_line[3].strip().split(":")
#         product_dict["name"] = name_line[1]
#         product_dict["price"] = price_line[1]
#         product_dict["amount"] = amount_line[1]
#         product_dict["year"] = year_line[1]
#         shopping_car.append(product_dict)
#     print(shopping_car)
#
# for i in range(len(shopping_car)):
#     total = total + int(shopping_car[i]["price"])
# print(total)


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
staff_car = []
staff_dict = {}
title_list =[]
value_list = []
number = 0
with open('a8.txt', mode='r', encoding='utf-8') as f:
    f.seek(0)
    for line in f:
        if line.strip() !="":
            new_line = line.strip().split(" ")
            if line.strip().startswith("序号"):
                for index,value in enumerate(new_line):
                    if value != '':
                        title_list.append(value)
                continue
            else:
                for index,value in enumerate(new_line):
                    if value != '':
                        value_list.append(value)
                value_list.insert(0,number)
                number +=1
            staff_dict =dict(zip(title_list,value_list))
            staff_car.append(staff_dict)
        else:
            pass
        value_list =[]
    print(staff_car)

# 7,查看当前文件夹某一文件编码
# import chardet
# path = "D:/Python14/Python_Project/Python18/day8/a1.txt"
# f = open(path,'rb')
# data = f.read()
# print(chardet.detect(data))
# print(f.fileno())

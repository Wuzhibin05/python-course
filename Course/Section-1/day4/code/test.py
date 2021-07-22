#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/7/20

# ****************************************************************************************
# 1，写代码，有如下列表，按照要求实现每一个功能

# ```python
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# ```
# - 1)计算列表的长度并输出

# - 3)请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# - 4)请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# - 5)请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# - 6)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# - 7)请删除列表中的元素"eric",并输出添加后的列表
# - 8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# - 9)请删除列表中的第2至4个元素，并输出删除元素后的列表
# - 10)请将列表所有得元素反转，并输出反转后的列表
# - 11)请计算出"alex"元素在列表li中出现的次数，并输出该次数。
li = ["alex" , "WuSir" , "ritian" , "barry" , "wenzhou" , "eric"]
l2 = [1 , "a" , 3 , 4 , "heart"]
s = "qwert"

# # 1
# print(len(li))
# # 2
# li.append("seven")
# print(li)
#
# # 3
# li.insert(1, "Tony")
# print(li)
#
# # 4
# li[1] = "Kelly"
# print(li)
#
# # 5
# li.extend(l2)
# print(li)
#
# # 6
# li.extend(s)
# print(li)
#
# # 7
# li.remove("eric")
# print(li)

# 8
# print(li.pop(1), li)

# 9
# del li[2:5]
# print(li)
# 10
# li.reverse()
# print(li)
#
# # 11
# print(li.count("alex"))

# ****************************************************************************************
# 2，写代码，有如下列表，利用切片实现每一个功能

# ```python
# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# ```
# - 1)通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
# - 2)通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
# - 3)通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
# - 4)通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
# - 5)通过对li列表的切片形成新的列表l5,l5 = ["c"]
# - 6)通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
# li = [1, 3, 2, "a", 4, "b", 5, "c"]
# print(li[:3])
# print(li[3:6])
# print(li[::2])
# print(li[1:6:2])
# print(li[7:])
# print(li[-3::-2])

# ****************************************************************************************
# 3,写代码，有如下列表，按照要求实现每一个功能。

# - lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# - 1)将列表lis中的"tt"变成大写（用两种方式）。
# - 2)将列表中的数字3变成字符串"100"（用两种方式）。
# - 3)将列表中的字符串"1"变成数字101（用两种方式）。
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
#
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[3][2][1][0] = "TT"
# lis[3][2][1][1] = "100"
# lis[3][2][1][2] = "101"
# print(lis)


# 4,请用代码实现：
#
# ```python
# li = ["alex", "eric", "rain"]
# ```
# 利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
# li = ["alex", "eric", "rain"]
# s = '_'.join(li)
# print(s)

# ## 5，利用for循环和range打印出下面列表的索引。

# ```python
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# ```
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for i in range(len(li)):
#     print(li[i])


# ## 6，利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
# li = []
# for i in range(100):
#     if i % 2 == 0:
#         li.append(i)
# print(li)


# ## 8，利用for循环和range从100~1，倒序打印。
# for i in range(100, 0, -1):
#     print(i)


# ## 9，利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。
# li =[]
# for i in range(100, 9, -1):
#     if i % 4 == 0:
#         li.append(i)
# li.reverse()
# print(li)


# # 10，利用for循环和range，将1-30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成*。
# li = []
# for i in range(1, 31):
#     if i % 3 == 0:
#         li.append("*")
#     else:
#         li.append(i)
# print(li)


# 11，查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，
# 并添加到一个新列表中,最后循环打印这个新列表。
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " Aqc", " aqc"]
# li2 = []
# for i in li:
#     s = i.strip()
#     if (s.startswith("a") or s.startswith("A")) and s.endswith("c"):
#         li2.append(s)
# print(li2)

# #12,开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符

# 敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# 则将用户输入的内容中的敏感词汇替换成等长度的*（苍老师就替换*），并添加到一个列表中；
# 如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
# li9 = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# li10 = []
# msg = input("请输入您的评论:").strip()
# for i in li9:
#     if i in msg:
#         msg =msg.replace(i, "*"*len(i))
# li10.append(msg)
# print(li10)


# ## 13，有如下列表
# ```python
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# ```
# 循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。
# 我想要的结果是：
# ```python
# 3
# "alex"
# 7,
# "taibai"
# ritian
# ```
li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
for i in li:
    if type(i) == list:
        for j in i:
            print(j)
    else:
        print(i)

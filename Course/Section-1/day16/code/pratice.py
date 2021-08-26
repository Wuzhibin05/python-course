#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/8/26

"""
3.用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
name=['alex','wupeiqi','yuanhao','nezha']
"""
# 方法一
# name = ['alex', 'wupeiqi', 'yuanhao', 'nezha']
#
# def add_str(x):
#     return x + "_sb"
# ret = map(add_str, name)
# print(list(ret))

# 方法二
# ret2 = map((lambda x: x + "_sb"), name)
# print(list(ret2))


"""
4.用filter函数处理数字列表，将列表中所有的偶数筛选出来
num = [1,3,5,6,7,8]
"""
num = [1, 3, 5, 6, 7, 8]
# 方法一
# def is_even(x):
#     if x % 2 == 0:
#         return True
# ret = filter(is_even, num)
# print(list(ret))

# 方法二
# lambda x:x if x % 2 == 0
# ret = filter((lambda x: True if x % 2 == 0 else False), num)
# print(list(ret))


"""
5.随意写一个20行以上的文件
运行程序，先将内容读到内存中，用列表存储。
接收用户输入页码，每页5条，仅输出当页的内容
"""
def get_page(n):
    file_list = []
    with open('text', encoding='utf-8') as f:
        for line in f:
            file_list.append(line)
    if (n-1)*5 <= len(file_list):
        return file_list[(n-1)*5:n*5]
    else:
        return "没有当前页,请重新输入\n"

while True:
    page_str = input("请输入你要看的页码(输入q退出):")
    if page_str.isdigit():
        page_num = int(page_str)
        ret = get_page(page_num)
        print(("当前显示的为第%d页"%page_num).center(80,"="))
        for i in ret:
            print(i,end='')
    elif page_str.isupper() == "Q":
        break
    else:
        print("输入错误，请重新输入")






"""
6.如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
"""

"""
# 6.1.计算购买每支股票的总价
"""


"""
# 6.2.用filter过滤出，单价大于100的股票有哪些
"""

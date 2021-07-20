#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com

# li = ['alex',[1,2,3],'wusir','egon','女神','taibai']
# l1 = li[0]
# print(l1)
# l2 = li[1]
# print(l2)
# l3 = li[0:3]
# print(l3)

li = ['alex','wusir','egon','女神','taibai']

#增加 append insert
li.append('日天')
li.append(1)
print(li)
# while 1:
#     username = input('>>>')
#     if username.strip().upper() == 'Q':
#         break
#     else:
#         li.append(username)
# print(li)
li.insert(4,'春哥')
print(li)
li.extend('二哥')
li.extend([1,2,3])
print(li)

#删
li = ['taibai','alex','wusir','egon','女神',]
# name = li.pop(1)  # 返回值
# name = li.pop()  # 默认删除最后一个
# print(name,li)

# li.remove('taibai')  # 按元素去删除
# print(li)

# li.clear()  # 清空
# print(li)

# del li
# del li[0:2]  # 切片去删除
# print(li)

# 改
# li[0] = '男兽'
# li[0] = [1,2,3]
# 切片
# li[0:3] = '云姐plfdslkmgdfjglk'
# li[0:3] = [1,2,3,'春哥','咸鱼哥']
# print(li)

# 查
# for i in li:
#     print(i)
# print(li[0:2])

# 公共方法：
# l = len(li)
# print(l)
# num = li.count('taibai')
# print(num)
# print(li.index('wusir'))
# li = [1,5,4,7,6,2,3]
# ## # li.sort()
# # # print(li)
# # #反向排序
# # # li.sort(reverse=True)正向排序

# # print(li)
# #反转
# li.reverse()
# print(li)


# 列表的嵌套
li = ['taibai','武藤兰','苑昊',['alex','egon',89],23]

# print(li[1][1])
# name = li[0].capitalize()
# # print(name)
# li[0] = name
# li[0] = li[0].capitalize()
# li[2] = '苑日天'
# print(li[2].replace('昊','ritian'))
# li[2] = li[2].replace('昊','ritian')
# li[3][0] = li[3][0].upper()
# print(li)


l1 = ["wuzb","test","dev","ce"]
while True:
    name = input("请输入你要增加的姓名,如果要退出请输入q:")

    if name.strip().upper() == "Q":
        break
    l1.append(name)
    print(l1)

# 列表转化成字符串:list -----> str    join
# 字符串转换为列表：str ----->list   split()

li = ['taibai','alex','wusir','egon','女神',]
s = '.'.join(li)
t = s.split('.')
print(s)
print(t)


# range  [1,2,3,4,5,6,.......100........]

# for i in range(3,10):
#     print(i)
# for i in range(10):
#     print(i)
# for i in range(0,10,3):
#     print(i)
# for i in range(10,0,-2):
#     print(i)
# for i in range(10,-1,-2):
#     print(i)

# li = [1,2,3,5,'alex',[2,3,4,5,'taibai'],'afds']
# for i in li:
#     if type(i) == list:
#         for k in i:
#             print(k)
#     else:print(i)

# for i in range(len(li)):
#     if type(li[i]) == list:
#         for j in li[i]:
#             print(j)
#     else:print(li[i])
#
#

# li = [1,2,3,5,'alex',[2,3,4,5,'taibai'],'afds']
# for i in range(len(li)):
#     if  type(li[i]) == list:
#         for j in li[i]:
#             print(j)
#     else:
#         print(li[i])





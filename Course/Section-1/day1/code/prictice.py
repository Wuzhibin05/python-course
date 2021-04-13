#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wu Zhi Bin"
# Email: wuzhibin05@163.com
# Date: 2021/4/2

# =============================== 题目 ==========================================
#  1,使用while循环输入1到10

# 2,求1-100的所有数的和

# 3,求1-100内所有奇数

# 4,求1-100内所有偶数

# 5,求1-2+3-4+5 ... 99的所有数的和。

# 6,要求用户输入0-100的数字后，你能正确打印他的对应成绩(考察 if 条件结构)
# A    90-100
# B    80-89
# C    60-79
# D    40-59
# E    0-39

# 7,用户登陆（三次机会重试）

# 8，猜年龄（指定匹配）

# ================================ 答案 =========================================
# 答案1

# count = 1
# while count <= 10:
#     print(count)
#     count += 1

# 答案2

# total, n = 0, 1
# while n <= 100:
#     total += n
#     n += 1
# print(total)

# 答案3

# total, n = 0, 1
# while n <= 100:
#     if n % 2 != 0:
#         print(n)
#         total += n
#     n += 1
# print(total)

# 答案4

# total, n = 0, 1
# while n <= 100:
#     if n % 2 == 0:
#         print(n)
#         total += n
#     n += 1
# print(total)

# 答案5

# total, n = 0, 1
# while n < 100:
#     if n % 2 == 0:
#         total -= n
#     else:
#         total += n
#     n += 1
# print(total)

# 答案6

# score = int(input("Please input you score:"))
# if score > 100:
#     print("总分才100")
# if score > 89:
#     print("You got A")
# elif score > 79:
#     print("You got B")
# elif score > 59:
#     print("You got C")
# elif score > 39:
#     print("You got D")
# else:
#     print("You got E")

# 答案7
# username, password = 'wuzb', 1
# count_time = 3
# while count_time > 0:
#     guess_name = input("Please input username you guess:")
#     count_time -= 1
#     if guess_name == username:
#         guess_password = int(input("Please input password you guess:"))
#         if guess_password == password:
#             print("You got login")
#             break
#     else:
#         print("username or password is wrong! ")

# username = "wuzhibin"
# password = "1"
# count3 = 0
# times = 4
# while count3 < 4:
#     user = input("Please input you name：")
#     passwd = input("please input your password:")
#     if user == username and passwd == password:
#         print("welcome to login in！")
#         count3 = 0
#         break
#     else:
#         count3 +=1
#         print("You only have %s times"%(times-count3))

# 答案8

# age = 32
# guess_age = int(input(">>>:"))
# if guess_age > age:
#     print("猜大了")
# elif guess_age < age:
#     print("猜小了")
# else:
#     print("猜对了")

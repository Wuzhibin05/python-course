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

# 7,用户登陆（三次机会重试）。

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

score = int(input("Please input you score:"))
if score > 100:
    print("总分才100")
if 90 < score < 100:
    print("You got A")
elif 80 < score < 89:
    print("You got B")
elif 60 < score < 79:
    print("You got C")
elif 40 < score < 59:
    print("You got D")
elif 0 < score < 39:
    print("You got E")
else:
    print("You are stupid")

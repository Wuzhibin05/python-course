#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/4/13

# # 1、判断下列逻辑语句的True,False.
# print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)  # T
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)  # F
#
# # 2、求出下列逻辑语句的值。
#
# print(8 or 3 and 4 or 2 and 0 or 9 and 7)  # 8
# print(0 or 2 and 3 and 4 or 6 and 0 or 3)  # 4
# 3、下列结果是什么？

print(6 or 2 > 1)  # 6
print(3 or 2 > 1)  # 3
print(0 or 5 < 4)  # False
print(5 < 4 or 3)  # 3
print(2 > 1 or 6)  # True
print(3 and 2 > 1)  # True
print(0 and 3 > 1)  # 0
print(2 > 1 and 3)  # 3
print(3 > 1 and 0)  # 0
print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)  # 2
2
#  5、利用if语句写出猜大小的游戏：
# 设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确，
# 然后退出循环。

number = 66
while True:
    guess_num = int(input("Please input number you guess:"))
    if guess_num > number:
        print("Too big")
    elif guess_num < number:
        print("Too small")
    else:
        print("You are so clever!")
        break

#  6、在5题的基础上进行升级：
# 给用户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循环，如果三次之内没有猜测正确，
# 则自动退出循环，并显示‘太笨了你....’。

number = 66
guess_time = 0
while True:
    if guess_time < 3:
        guess_num = int(input("Please input number you guess:"))
        guess_time += 1
        if guess_num > number:
            print("Too big")
        elif guess_num < number:
            print("Too small")
        else:
            print("You are so clever!")
            break
    else:
        print("You are so stupid!")
        break

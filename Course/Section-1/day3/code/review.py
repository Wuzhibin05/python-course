#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/7/16

print(5 < 4 or 3)  # 3
print(2 > 1 or 6)  # true
print(3 > 1 and 0)  # 0
# #计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和

total = 0
i = 1
while i < 100:
    if i % 2 == 0:
        if i != 88:
            total -= i
    else:
        total += i
    i += 1
print(total)

# #计算 1 - 2 + 3  ... -99 中除了88意外所有数的总和
total = 0
i = 1
while i < 100:
    if i % 2 == 0:
        if i != 88:
            total -= i
    else:
        if i == 99:
            total -= i
        total += i
    i += 1
print(total)



# ⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）

username = 'wuzhibin'
password = '123'
i = 0
times = 3
while i < 3:
    user = input("请输入用户名：")
    passwd = input("请输入密码：")
    if user == username and passwd == password:
        print("欢迎登陆系统，%s!" % user)
        break
    else:
        i += 1
        if i < 3:
            print("用户名或者密码错误，你还有%s次机会！" % (times-i))
        else:
            choice = input("你已经没有机会了，想再试试吗?请输入Y:")
            if choice == 'Y':
                i = 0
else:
    print("你已经被强制退出！")



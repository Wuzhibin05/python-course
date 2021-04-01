#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: $(DATE)
#  1,使用while循环输入1到10

count = 0
while count < 10:
    count += 1
    if count == 7:
        continue
    print(count)

# 2,求1-100的所有数的和

sum,count1= 0,0
while count1<100:
    count1 +=1
    sum +=count1
print(sum)


# 3,求1-100内所有奇数
odd =0
while odd < 100:
    odd +=1
    if odd%2 ==0:
        pass
    else:
        print(odd)

# 4,求1-100内所有偶数
even =0
while even < 100:
    even += 1
    if even % 2 == 1:
        pass
    else:
        print(even)

# 5,求1-2+3-4+5 ... 99的所有数的和。
count2, total = 0, 0
while count2 < 99:
    count2 += 1
    if count2 % 2 == 1:
        total += count2
    else:
        total -= count2
    print(count2,total)
print(total)

# 6,用户登陆（三次机会重试）。

username = "wuzhibin"
password = "1"
count3 = 0
times = 4
while count3 < 4:
    user = input("Please input you name：")
    passwd = input("please input your password:")
    if user == username and passwd == password:
        print("welcome to login in！")
        count3 = 0
        break
    else:
        count3 +=1
        print("You only have %s times"%(times-count3))
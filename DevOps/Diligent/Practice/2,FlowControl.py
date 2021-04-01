#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: 2019/3/12

# 1． 布尔数据类型的两个值是什么？如何拼写？
# True and False

# 2． 3 个布尔操作符是什么？Python 编程快速上手——让繁琐工作自动化
# and or not  优先级：not > or > and

# 3．写出每个布尔操作符的真值表（也就是操作数的每种可能组合，以及操作
# 的结果）。

# 4．以下表达式求值的结果是什么？
# (5 > 4) and (3 == 5) False
# not (5 > 4)          False
# (5 > 4) or (3 == 5)  True
# not ((5 > 4) or (3 == 5))  False
# (True and True) and (True == False)  False
# (not False) or (not True) True

# 5． 6 个比较操作符是什么？
#  > < == != >= <=

# 6．等于操作符和赋值操作符的区别是什么？
# 等于是判断两个值是否相等，赋值是变量的值存到变量所指定的内存地址中

# 7．解释什么是条件，可以在哪里使用条件。
# 程序在满足了一定规则的情况下才会执行。

# 8．识别这段代码中的 3 个语句块：
# spam = 10
# # if spam == 10:
# #     print('eggs')
# # if spam > 5:
# #     print('bacon')
# # else:
# #     print('ham')
# #     print('spam')
# #     print('spam')

# 9．编写代码，如果变量 spam 中存放 1，就打印 Hello，如果变量中存放 2，就
# 打印 Howdy，如果变量中存放其他值，就打印 Greetings!
# spam = 2
# if spam == 1:
#     print('hello')
# elif spam == 2:
#     print('Howdy')
# else:
#     print('Greetings')

# 10． 如果程序陷在一个无限循环中， 你可以按什么键？
# break
# 11． break 和 continue 之间的区别是什么？
# break 将所在循环的条件置为false并退出循环。continue是结束本次循环，继续下一次循环。

# 12． 在 for 循环中， range(10)、 range(0, 10)和 range(0, 10, 1)之间的区别是什么？
# 0-9   结果一样。

# 13．编写一小段程序，利用 for 循环，打印出从 1 到 10 的数字。然后利用 while
# 循环，编写一个等价的程序，打印出从 1 到 10 的数字。
# for i in range(1,11):
#     print(i)
# j = 0
# while j<10:
#     j +=1
#     print(j)

# 14． 如果在名为 spam 的模块中， 有一个名为 bacon()的函数，那么在导入 spam
# 模块后， 如何调用它？ # span.bacon()

# 附加题：在因特网上查找 round()和 abs()函数，弄清楚它们的作用。在交互式
# 环境中尝试使用它们。


# eg1 退出程序。
import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

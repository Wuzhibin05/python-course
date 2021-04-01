#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: 2019/3/14
#
# 1． 为什么在程序中加入函数会有好处？
#   答：提高代码的重用性，可读性以及

# 2．函数中的代码何时执行：在函数被定义时，还是在函数被调用时？
#   答：执行的时候

# 3．什么语句创建一个函数？
# 4．一个函数和一次函数调用有什么区别？
# 5． Python 程序中有多少全局作用域？有多少局部作用域？
# 6．当函数调用返回时，局部作用域中的变量发生了什么？
# 7．什么是返回值？返回值可以作为表达式的一部分吗？
# 8．如果函数没有返回语句，对它调用的返回值是什么？
# 9．如何强制函数中的一个变量指的是全局变量？
# 10． None 的数据类型是什么？
# 11． import areallyourpetsnamederic 语句做了什么？
# 12．如果在名为 spam 的模块中，有一个名为 bacon()的函数，在引入 spam 后，
# 如何调用它？
# 13．如何防止程序在遇到错误时崩溃？
# 14． try 子句中发生了什么？ except 子句中发生了什么？

# 3.11.1 Collatz 序列

''' 1,编写一个名为 collatz()的函数，它有一个名为 number 的参数。如果参数是偶数，
# 那么 collatz()就打印出 number // 2， 并返回该值。如果 number 是奇数， collatz()就打
# 印并返回 3 * number + 1。
2,然后编写一个程序， 让用户输入一个整数， 并不断对这个数调用 collatz()， 直
到函数返回值１（令人惊奇的是， 这个序列对于任何整数都有效， 利用这个序列，
你迟早会得到 1！ 既使数学家也不能确定为什么。 你的程序在研究所谓的“Collatz
序列”，它有时候被称为“最简单的、 不可能的数学问题”）。第 3 章 函数
记得将 input()的返回值用 int()函数转成一个整数，否则它会是一个字符串。
提示 如果 number % 2 == 0，整数 number 就是偶数，如果 number % 2 == 1，它
就是奇数。
# 这个程序的输出看起来应该像这样：
# Enter number:
# 3
# 10
# 5
# 16
# 8 4 2 1
'''

# def collatz(number):
#     if number%2 == 0:
#         result = number // 2
#     else:
#         result = 3*number+1
#     print(result)
#     return  result
#
# while True:
#     number = input("请输入一个整数>>")
#     if number.isdigit():
#         collatz(int(number))
#     else:
#         print("您的输入不合法，请重新输入。")

#### 3.11.2 输入验证

''' 在前面的项目中添加 try 和 except 语句，检测用户是否输入了一个非整数的字
符串。正常情况下， int()函数在传入一个非整数字符串时，会产生 ValueError 错误，
比如 int('puppy')。在 except 子句中，向用户输出一条信息，告诉他们必须输入一个
整数 '''

def collatz(number):
    if number%2 == 0:
        result = number // 2
    else:
        result = 3*number+1
    print(result)
    return  result

while True:
    number = input("请输入一个整数>>")
    try :
        int(number)
    except ValueError:
        print("您输入的内容不合法，请重新输入！")
        continue
    collatz(int(number))
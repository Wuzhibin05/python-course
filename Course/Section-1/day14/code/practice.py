#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/8/16
"""
11–1.参数。比较下面 3 个函数：
def countToFour1():
    for eachNum in range(5):
        print(eachNum)
def countToFour2(n):
    for eachNum in range(n, 5):
        print (eachNum)
def countToFour3(n=1):
    for eachNum in range(n, 5):
        print (eachNum)
给定如下的输入直到程序输出，你认为什么会发生？向下表 11.2 填入输出。如果你认为给定的
输入会发生错误的话填入“ERROR"或者如果没有输出的话填入“NONE"Edit By Vheavens
Edit By Vheavens
"""

def countToFour1():
    for eachNum in range(5):
        print(eachNum)
def countToFour2(n):
    for eachNum in range(n, 5):
        print(eachNum)
def countToFour3(n=1):
    for eachNum in range(n, 5):
        print(eachNum)

countToFour1()
countToFour2(1)
countToFour3()

"""
11-2.函数。结合你对练习 5-2 的解，以便你创建一个带相同对数字并同时返回一它们之和以及
产物的结合函数。
"""
# def countToFour4():


"""
表 11.2 问题 11-1 的输出图
11-3 函数。在这个练习中，我们将实现 max()和 min()内建函数。
(a) 写分别带两个元素返回一个较大和较小元素，简单的 max2()核 min2()函数。他们应该可以
用任意的 python 对象运作。举例来说，max2(4,8)和 min2(4,8)会各自每次返回 8 和 4。
(b) 创建使用了在 a 部分中的解来重构 max()和 min()的新函数 my_max()和 my_min().这些函
数分别返回非空队列中一个最大和最小值。它们也能带一个参数集合作为输入。用数字和字符串来
测试你的解。
"""



"""
11–4. 返回值。给你在 5-13 的解创建一个补充函数。创建一个带以分为单位的总时间以及
返回一个以小时和分为单位的等价的总时间。
"""
"""
11–5.
默认参数。 更新你在练习 5-7 中创建的销售税脚本以便让销售税率不再是函数输入的必要之物。
创建使用你地方税率的默认参数如果在调用的时候没有值传入。
"""
"""
11–6. 变长参数。下一个称为 printf()的函数。有一个值参数，格式字符串。剩下的就是根
据格式化字符串上的值，要显示在标准输出上的可变参数，格式化字符串中的值允许特别的字符串
格式操作指示符，如%d, %f, etc。提示：解是很琐碎的----无需实现字符串操作符功能性，但你需
要显示用字符串格式化操作（%）
"""
"""
11–7. 用 map() 进 行 函 数 式 编 程 。 给 定 一 对 同 一 大 小 的 列 表 ， 如 [1 ， 2 ， 3] 和
['abc','def','ghi',....]，将两个标归并为一个由每个列表元素组成的元组的单一的表，以使我
们的结果看起来像这样：{[(1, 'abc'), (2, 'def'), (3, 'ghi'), ...}.（虽然这问题在本质上和
第六章的一个问题相似，那时两个解没有直接的联系）然后创建用 zip 内建函数创建另一个解。Edit By Vheavens
Edit By Vheavens
"""
"""
11–8. 用 filer()进行函数式编程.使用练习 5-4 你给出的代码来决定闰年。更新你的代码一
边他成为一个函数如果你还没有那么做的话。然后写一段代码来给出一个年份的列表并返回一个只
有闰年的列表。然后将它转化为用列表解析。
"""
"""
11–9. 用 reduce()进行函数式编程。复习 11.7.2 部分，阐述如何用 reduce()数字集合的累
加的代码。修改它，创建一个叫 average()的函数来计算每个数字集合的简单的平均值。
"""
"""
11–10.用 filter()进行函数式编程。在 unix 文件系统中，在每个文件夹或者目录中都有两个
特别的文件：'.'表示现在的目录，'..'表示父目录。给出上面的知识，看下 os.listdir()函数的文
档并描述这段代码做了什么：
files = filter(lambda x: x and x[0] != '.', os. listdir(folder))
"""
"""
11–11.用 map()进行函数式编程。写一个使用文件名以及通过除去每行中所有排头和最尾的空
白来“清洁“文件。在原始文件中读取然后写入一个新的文件，创建一个新的或者覆盖掉已存在的。
给你的用户一个选择来决定执行哪一个。将你的解转换成使用列表解析。
"""
"""
11–12. 传递函数。给在这章中描述的 testit()函数写一个姊妹函数。timeit()会带一个函数
对象（和参数一起）以及计算出用了多少时间来执行这个函数，而不是测试执行时的错误。返回下
面的状态：函数返回值，消耗的时间。你可以用 time.clock()或者 time.time()，无论哪一个给你
提供了较高的精度。（一般的共识是在 POSIX 上用 time.time()， 在 win32 系统上用 time.clock()）
注意：timeit()函数与 timeit 模块不相关(在 python2.3 中引入）
"""
"""
11–13.使用 reduce()进行函数式编程以及递归。在第 8 张中，我们看到 N 的阶乘或者 N!作为
从 1 到 N 所有数字的乘积。
(a) 用一分钟写一个带 x,y 并返回他们乘积的名为 mult(x,y)的简单小巧的函数。
(b)用你在 a 中创建 mult()函数以及 reduce 来计算阶乘。
(c)彻底抛弃掉 mult()的使用，用 lamda 表达式替代。
(d)在这章中， 我们描绘了一个递归解决方案来找到 N!用你在上面问题中完成的 timeit()函数，
并给三个版本阶乘函数计时(迭代的，reduce()以及递归）
"""
"""
11–14. 递归。我们也来看下在第八章中的 Fibonacci 数字。重写你先前计算 Fibonacci 数字
的解(练习 8-9）以便你可以使用递归。
"""
"""
11–15.递归。从写练习 6-5 的解，用递归向后打印一个字符串。用递归向前以及向后打印一个
字符串。
"""
"""
11–16. 更新 easyMath.py。这个脚本，如例子 11.1 描绘的那样，以入门程序来帮助年轻人强
化他们的数学技能。通过加入乘法作为可支持的操作来更进一步提升这个程序。额外的加分：也加
入除法；这比较难做些因为你要找到有效的整数除数。幸运的是，已经有代码来确定分子比分母大，
所以不需要支持分数。Edit By Vheavens
Edit By Vheavens
"""
"""
11–17.定义
(a) 描述偏函数应用和 currying 之间的区别。
(b) 偏函数应用和闭包之间有什么区别？
(c) 最后，迭代器和生成器是怎么区别开的？
"""
"""
11–18. 同步化函数调用。复习下第六章中当引入浅拷贝和深拷贝的时候，提到的丈夫和妻子
情形（6.20 小结）。他们共用了一个普通账户，同时对他们银行账户访问时会发生不利影响。
创建一个程序，让调用改变账户收支的函数必需同步。换句话说，在任意给定时刻只能有个
一进程或者线程来执行函数。一开始你试着用文件，但是一个真正的解决方法是用装饰器和在
threading 或者 mutex 模块中的同步指令。你看看第 17 张来获得更多的灵感
"""

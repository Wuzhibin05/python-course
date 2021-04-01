#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: 2019/1/31

# 1，设存在列表形如 list_1 = [[1, 2], [3, 4, 5], [6, 7], [8], [9]] ，则

# 使用遍历查询列表元素
#控制台输出[1, 2]，[3, 4, 5]，[6, 7]，[8]，[9]
list_1 = [[1, 2], [3, 4, 5], [6, 7], [8], [9]]
for i in list_1:
    print(i)

# 将多层嵌套拆开的方法有：

# 1.列表推导法：

list_1 = [[1, 2], [3, 4, 5], [6, 7], [8], [9]];
list_2 = [i for j in list_1 for i in j] ;
print(list_2)

# 2.第三模块组合法
#
# list_1 = [[1, 2], [3, 4, 5], [6, 7], [8], [9]];
# list_2 = []
# for _ in list_1:
#     list_2 += _
# print(list_2)
# 1
# 2
# 3
# 4
# 5
# 3.使用sum
#
# > list_1 = [[1, 2], [3, 4, 5], [6, 7], [8], [9]] ;
# > list_2 = sum(list_1,[]) ;
# > print(list_2)
# 1
# 2
# 3
# 4.对于复杂一些的，如：list =[1,[2],[[3]],[[4,[5],6]],7,8,[9]]，上面的方法就不好使了。得换个方法了，这里使用递归的方法解决。
#
# > def flat(nums):
# >     res = []
# >     for i in nums:
# >         if isinstance(i, list):
# >             res.extend(flat(i))
# >         else:
# >             res.append(i)
#     return res


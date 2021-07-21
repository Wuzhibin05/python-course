#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com

# =============== 字典 dict ===========================================
"""
# 数据类型划分：可变数据类型，不可变数据类型
    1，不可变数据类型：元组，bool int str       可哈希
    2，可变数据类型：list，dict set             不可哈希

# 字典特点
1，dict key 必须是不可变数据类型，可哈希.
2，value：任意数据类型。

# dict 优点：
1,二分查找去查询
2,存储大量的关系型数据
3,特点：无序的
"""

# =============== 字典定义 ===========================================
dic = {
    'name': ['大猛', '小孟'],
    'py9': [{'num': 71, 'avg_age': 18, },
            {'num': 71, 'avg_age': 18, },
            {'num': 71, 'avg_age': 18, },
            ],
    True: 1,
    (1, 2, 3): 'wuyiyi',
    2: '二哥',
}

# =============== 字典常用方法 ===========================================
dic1 = {'age': 16, 'name': 'jin', 'sex': 'male'}
# ======================= 增加 ====================
# 1，增：
# dic1['high'] = 185  # （1）,直接指定新的key和value
# # dic1.setdefault('weight')  # （2），有键值对，不做任何改变，没有才添加。
# dic1.setdefault('weight', 150)
# dic1.setdefault('name', '二哥')
# print(dic1)

# ===================== 删除 ======================
# 2，删
# print(dic1.pop('age'))  # (1)有返回值，按键去删除
# print(dic1.pop('二哥', None))  # 可设置返回值

# print(dic1.popitem())  # (2)随机删除 有返回值 元组里面是删除的键值。


# del dic1['name']  # (3)del删除
# print(dic1)
# del dic1

# dic1.clear()  # （4）清空字典

# print(dic1)

# ==================== 改了 =======================
# 3,改  update
# dic1['age'] = 32  # （1）直接指定新值

# dic = {"name": "jin", "age": 18, "sex": "male"}
# dic2 = {"name": "alex", "weight": 75}
# dic2.update(dic)  # （2）用1来覆盖2
#
# print(dic)
# print(dic2)

# print(dic1)

# ==================== 查 =======================
# print(dic1.keys(), type(dic1.keys()))  # key
# print(dic1.values())  # value
# print(dic1.items())  # items
#
# # 取key
# for i in dic1:
#     print(i)
# for i in dic1.keys():
#     print(i)
#
# # 取出value
# for i in dic1.values():
#     print(i)
# for i in dic1:
#     print(dic1[i])

# a,b = 1,2
# print(a,b)

# #变量交换位置方法
# a = 1
# b = 2
# a, b = b, a
# print(a, b)
# a,b = [1,2],[2,3]
# # a,b = (1,2)
# print(a,b)

# # 分别取出key和values
# for k,v in dic1.items():
#     print(k,v)

v1 = dic1['name']
print(v1)

# v2 = dic1['name1']  # 取不到报错
# print(v2)

print(dic1.get('name1', '没有这个键'))

# =============================================================================

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: 2019/3/20

# 习题
# 1．空字典的代码是怎样的？
s={}
print(type(s))

# 2． 一个字典包含键'fow'和值 42， 看起来是怎样的？
{'fow':42}

# 3． 字典和列表的主要区别是什么？
# 字典存储的是键值对（映射关系），且键不能重复必须是不可变数据类型，无序。
# 有序的数据的集合，元素可以重复有序，可以存储任何数据类型。

# 4． 如果 spam 是{'bar': 100}， 你试图访问 spam['foo']， 会发生什么？
# 系统会报错KeyError: 'foo'

# 5． 如果一个字典保存在 spam 中， 表达式'cat' in spam 和'cat' in spam.keys()之间
# 的区别是什么？
# 没有区别

# 6． 如果一个字典保存在变量中， 表达式'cat' in spam 和'cat' in spam.values()之间
# 的区别是什么？
# in dict:查询该对象是否在字典的key里面。in dic.values :查询该对象是否在字典的值中。

# 7． 下面代码的简洁写法是什么？
# if 'color' not in spam:
# spam['color'] = 'black'
# spam.setdefault('color','black')

# 8． 什么模块和函数可以用于“漂亮打印”字典值？
# pprint pprint.pprint(spm)

# 5.6 实践项目
# 作为实践， 编程完成下列任务。
# 5.6.1 好玩游戏的物品清单
# 你在创建一个好玩的视频游戏。用于对玩家物品清单建模的数据结构是一个字
# 典。其中键是字符串，描述清单中的物品，值是一个整型值，说明玩家有多少该物
# 品。例如，字典值{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}意味着玩
# 家有 1 条绳索、 6 个火把、 42 枚金币等。
# 写一个名为 displayInventory()的函数，它接受任何可能的物品清单， 并显示如下：94 Python 编程快速上手——让繁琐工作自动化
# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62
# 提示 你可以使用 for 循环， 遍历字典中所有的键。
# # inventory.py
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# def displayInventory(inventory):
#     print("Inventory:")
#     item_total = 0
#     for k, v in inventory.items():
#         print(str(v) + ' ' + k)
#         item_total += v
#     print("Total number of items: " + str(item_total))
# displayInventory(stuff)


# 5.6.2 列表到字典的函数，针对好玩游戏物品清单
# 假设征服一条龙的战利品表示为这样的字符串列表：
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# 写一个名为 addToInventory(inventory, addedItems)的函数， 其中 inventory 参数
# 是一个字典， 表示玩家的物品清单（像前面项目一样）， addedItems 参数是一个列表，
# 就像 dragonLoot。
# # addToInventory()函数应该返回一个字典， 表示更新过的物品清单。请注意， 列
# # 表可以包含多个同样的项。你的代码看起来可能像这样：
# def addToInventory(inventory, addedItems):
# # your code goes here
# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)
# 前面的程序（加上前一个项目中的 displayInventory()函数） 将输出如下：
# Inventory:
# 45 gold coin
# 1 rope
# 1 ruby
# 1 dagger
# Total number of items: 48

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def displayInventory(inventory):
    '''
    Args:
        inventory: dict
    Function：Output a dictionary in a fixed format
    Returns: None
    '''
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))
def addToInventory(inventory, addedItems):

    for i in range(len(addedItems)):
        if addedItems[i] not in inventory:
            inventory[addedItems[i]] = 1
        else:
            inventory[addedItems[i]] += 1
    return inventory

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/7/21

# #  1，有如下变量（tu是个元祖），请实现要求的功能
# ```python
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# ```
# - a. 讲述元祖的特性
# - b. 请问tu变量中的第一个元素 "alex" 是否可被修改？
# - c. 请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
# - d. 请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"

tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])

# a 不可变列表，即数据可以被查询，但不能被修改，儿子可以改，父亲不可改。
# b,不可以
# c,列表
# tu[1][2]["k2"].append("Seven")
# print(tu)
# c,元祖，不可以改


### 2， 字典
# ```python
# dic,dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# ```
# - a.请循环输出所有的key
# - b.请循环输出所有的value
# - c. 请循环输出所有的key和value
# - d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# - e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# - f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
# - g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典

# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# for key in dic:
#     print(key)
# for value in dic.keys():
#     print(value)
# for value in dic.values():
#     print(value)
# for key, value in dic.items():
#     print(key, value)
# dic["k4"]="v4"
# dic["k1"]="alex"
# dic["k3"].append(44)
# dic["k3"].insert(1, 18)
#
# print(dic)

# ## 3，字典
# - e,给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
# - f,删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]键值对。
# - g,给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

# av_catalog["大陆"]["1048"] = "一天就封了"
# del av_catalog["欧美"]["letmedothistoyou.com"]
# av_catalog["大陆"]["1024"].append("可以爬下来")
# print(av_catalog)


# ## 4、有字符串"k:1|k1:2|k2:3|k3:4" 处理成字典 {'k':1,'k1':2....}
# s = "k:1|k1:2|k2:3|k3:4"
# l = s.strip().split("|")
# dic1 = {}
# for i in l:
#     l2 = i.strip().split(":")
#     dic1[l2[0]] = l2[1]
#     print(i)
# print(l,dic1)



# ## 5、元素分类
# 有如下值li= [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# 即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
# li1= [11,22,33,44,55,66,77,88,99,90]
# dic4 ={"k1":[],"k2":[]}
#
# for i in li1:
#     if i > 66:
#         dic4["k1"].append(i)
#     elif i < 66:
#         dic4["k2"].append(i)
#     else:
#         continue
# print(dic4)

# ## 6、输出商品列表，用户输入序号，显示用户选中的商品


# #### 要求:
# - 1：页面显示 序号 + 商品名称 + 商品价格，如：
# 电脑 1999
# 鼠标 10
# - 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# - 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# - 4：用户输入Q或者q，退出程序。
goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998}]
flag = 1
for index,value in enumerate(goods):
    print(index, value["name"], value["price"])
while flag:
    good_num = input("请输入商品编号:")
    if good_num.isdigit():
        good_index = int(good_num)
        if good_index in range(len(goods)):
            print(goods[good_index]["name"], goods[good_index]["price"])
        else:
            print("输入的商品编号不存在")
    elif good_num.upper() == "Q":
        flag = 0
    else:
        print("输入有误，请重新输入")






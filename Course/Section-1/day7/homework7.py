#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wuzhibin"
# Email: wuzhibin05@163.com
# Date: 2018/12/18

# 1、把列表中所有姓周的人的信息删掉(升级题：此题有坑, 请慎重):

lst = ['周老二', '周星星', '麻花藤', '周扒皮']
lst1=[]
s='周'
for i in lst:
    if  s in i:
        continue
    else:
        lst1.append(i)
lst = lst1
#print(lst)

# 2、车牌区域划分, 现给出以下车牌. 根据车牌的信息, 分析出各省的车牌持有量. (升级题)
# 结果: {'山东': 2, '北京': 1, '黑龙江': 2, '上海': 1}
cars = ['鲁A32444','鲁B12333','京B8989M','黑C49678','黑C46555','沪 B25041']
locals = {'沪':'上海', '黑':'黑龙江', '鲁':'山东', '鄂':'湖北', '湘':'湖南', '京': '北京'}

new_cars = []
count = {}
for i in range(len(cars)):
    new_cars.append(cars[i][0])
for i in locals.keys():
    count.setdefault(locals[i],new_cars.count(i))

print(count)

#3、干掉主播. 现有如下主播收益信息:
zhubo = {'卢本伟':522000, '冯提莫':189999, '金老板': 99999, '吴老板': 250000, 'alex': 126}
# 1. 计算主播平均收益值
# 2. 干掉收益小于平均值的主播
# 3. 干掉卢本伟
total = 0
del_zhubo = []
for i in zhubo:
    total += zhubo[i]
avg_salary = total / len(zhubo)
for i in zhubo.keys():
    if zhubo[i] < avg_salary:
        del_zhubo.append(i)
for i in del_zhubo:
    zhubo.pop(i)
zhubo.pop('卢本伟')
print(avg_salary)
print(zhubo)




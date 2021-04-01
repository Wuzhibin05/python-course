#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: 2019/2/14

# 1，使用random模块实现一个4位随机验证码
import random

def code_generater(bit):

    bit_of_code = 8
    code_list = []
    code = ''
    for i in range(bit_of_code):
        if i%2 == 0:
            code_list.append(chr(random.randrange(65,90)))
        else:
            code_list.append(random.randrange(0,10))
    random.shuffle(code_list)

    for i in range(len(code_list)):
        code +=str(code_list[i])
    return code
ret = code_generater(8)
print(ret)

# 实例二
def v_code():

    code = ''
    for i in range(5):

        num=random.randint(0,9)
        alf=chr(random.randint(65,90))
        add=random.choice([num,alf])
        code="".join([code,str(add)])

    return code

print(v_code())

# 2，给出两个时间，计算时差。
import time
# s = "Fri Jul 14 10:40:00 2017"
# time_before = time.mktime(time.strptime(s,"%a %b %d %H:%M:%S %Y"))
# time_now = time.time()
# print(time_before,time_now)
# diff_time = time_now - time_before
# struct_time = time.gmtime(diff_time)
# print(struct_time)
# print("时间差为%d年%d月%d天%d小时%d分钟%d秒"%(struct_time.tm_year-1970,struct_time.tm_mon-1,struct_time.tm_wday-1,
#                                           struct_time.tm_hour,struct_time.tm_min,struct_time.tm_sec))


import sys
ret2 = sys.path
print(ret2)
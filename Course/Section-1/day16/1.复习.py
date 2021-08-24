# 数据类型 ：int bool 。。。
# 数据结构 : dict list tuple set str



# print(eval('1+2+3'))
#
# code1 = 'for i in range(10):print(i)'
# complie1 = compile(code1,"",'exec')
# exec(complie1)
#
# import time
# for i in range(0,101,2):
#     time.sleep(0.1)
#     char_num = i//2      #打印多少个'*'
#     per_str = '\r%s%% : %s\n' % (i, '*' * char_num) if i == 100 else '\r%s%% : %s'%(i,'*'*char_num)
#     print(per_str,end='', flush=True)
# t=(1,2,3)
# print(hash(t))
#

# l = (1,2,23,213,5612,342,43)
# def is_old(i):
#     return i % 2 ==1
# ret = list(filter(is_old,l))
# print(ret)

import math

def is_sqrt(x):
    return math.sqrt(x) % 2 == 0
print(list(filter(is_sqrt,range(1,101))))
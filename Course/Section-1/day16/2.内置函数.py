# reversed()
# l = [1, 2, 3, 4, 5]
# l.reverse()
# print(l)
# l = [1, 2, 3, 4, 5]
# l2 = reversed(l)
# print(l2)
# 保留原列表，返回一个反向的迭代器

# l = (1,2,23,213,5612,342,43)
# sli = slice(1,5,2)
# print(l[sli])
# print(l[1:5:2])

# print(format('test', '<20'))
# print(format('test', '>40'))
# print(format('test', '^40'))

# bytes 转换成bytes类型
# 我拿到的是gbk编码的，我想转成utf-8编码
# print(bytes('你好',encoding='GBK'))     # unicode转换成GBK的bytes
# print(bytes('你好',encoding='utf-8'))   # unicode转换成utf-8的bytes

# 网络编程 只能传二进制 byte
# 照片和视频也是以二进制存储 byte
# html网页爬取到的也是编码 byte
# b_array = bytearray('你好',encoding='utf-8')
# print(b_array)
# print(b_array[0])
# '\xe4\xbd\xa0\xe5\xa5\xbd'
# s1 = 'alexa'
# s2 = 'alexb'

# l = 'ahfjskjlyhtgeoahwkvnadlnv'
# l2 = l[:10]
# print(l2)

# 切片 —— 字节类型  不占内存
# 字节 —— 字符串 占内存

# print(ord('好'))
# print(ord('1'))
# print(chr(97))

# print(ascii('好'))
# print(ascii('1'))
# name = 'egg'
# print('你好%r'%name)
# print(repr('1'))
# print(repr(1))

# print(all(['a','',123]))
# print(all(['a',123]))
# print(all([0,123]))

# print(any(['',True,0,[]]))

# l = [1,2,3,4,5]
# l2 = ['a','b','c','d']
# l3 = ('*','**',[1,2])
# d = {'k1':1,'k2':2}
# for i in zip(l,l2,l3,d):
#     print(i)

# def is_odd(x):
#     return x % 2 == 1
#
# def is_str(s):
#     return s and str(s).strip()
#
# ret = filter(is_odd, [1,  6, 7, 12, 17])
# ret = filter(is_str, [1, 'hello','','  ',None,[], 6, 7, 'world', 12, 17])
# print(ret)
# for i in ret:
#     print(i)
# [i for i in [1, 4, 6, 7, 9, 12, 17] if i % 2 == 1]


# def is_odd(x):
#     return x % 2 == 0
#
#
# ret = filter(is_odd, [1, 3, 5, 43, 43, 3, 8, 3, 10])
# for i in ret:
#     print(i)
# from math import sqrt
# def func(num):
#     res = sqrt(num)
#     return res % 1 == 0
# ret = filter(func,range(1,101))
# for i in ret:
#     print(i)


# ret = map(abs,[1,-4,6,-8])
# print(ret)
# for i in ret:
#     print(i)
l =[1,123,"a","b",4,19,]
dict={1:100,2:200}
# l.sort()
# print(l)
# for index,i in enumerate(dict):
#     print(index,i)

# filter 执行了filter之后的结果集合 <= 执行之前的个数
# filter只管筛选，不会改变原来的值
# map 执行前后元素个数不变
# 值可能发生改变

# l = [1,-4,6,5,-10]
# # l.sort(key = abs)   # 在原列表的基础上进行排序
# # print(l)
#
# print(sorted(l,key=abs,reverse=True))      # 生成了一个新列表 不改变原列表 占内存
# print(l)

# --------------------------------------根据列表长度排序--------------------------------------
l = ['   ',[1,2],'hello world']
new_l = sorted(l,key=len)
print(new_l)

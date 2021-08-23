
# # 两个数的和
# def add(x,y):
#     return x+y
# add = lambda x, y:x+y
#
# print(add(1, 2))
#
# dic={'k1':10,'k2':100,'k3':30}
# def func(key):
#     return dic[key]
# print(max(dic,key=func))   #根据返回值判断最大值，返回值最大的那个参数是结果
# print(max(dic,key=lambda key:dic[key]))
# print(max([1,2,3,4,5,-6,-7],key=abs))
#
# print(max(dic,key=lambda  key:dic[key]))

# ret = map(abs,[-1,2,-3,4])
# for i in ret:
#     print(i)

# def func(x):
#     return x**2
# ret = map(func,[-1,2,-3,4])
# for i in ret:
#     print(i)
#
# ret = map(lambda x:x**2,[-1,2,-3,4])


# def func(x):
#     return x>10
#
# res = filter(func,[5,8,11,9,15])
# for i in res:
#     print(i)


# min max filter map sorted —— lambda

# d = lambda p:p*2
# t = lambda p:p*3
# x = 2
# x = d(x) #x = 4
# x = t(x) #x = 12
# x = d(x) #x = 24
# print(x)

# ret = zip((('a'),('b')),(('c'),('d')))
# ret = map(lambda t:{t[0]:t[1]},ret)
# print(list(ret))


# 现有两元组(('a'),('b')),(('c'),('d')),
# 请使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]
ret = zip((('a'), ('b')), (('c'), ('d')))
# ------------------------------方式一--------------------------------------
# def func(tu):
#     return {tu[0]:tu[1]}
# res = map(func,ret)
# print(list(res))
# ------------------------------方式二--------------------------------------
res = map(lambda tu: {tu[0]: tu[1]}, ret)
print(list(res))
# ------------------------------方式二--------------------------------------
print(list(map(lambda tu: {tu[0]: tu[1]},
      zip((('a'), ('b')), (('c'), ('d'))))))


# max min sorted filter map
# 匿名函数 == 内置函数
# zip
# ret = zip((('a'),('b')),(('c'),('d')))
# res = map(lambda tup:{tup[0]:tup[1]},ret)
# print(list(res))

# def multipliers():
#     return [lambda x:i*x for i in range(4)]
# print([m(2) for m in multipliers()])

"""
3.以下代码的输出是什么？请给出答案并解释。
def multipliers():
    return [lambda x:i*x for i in range(4)]   # 0,1,2,3
print([m(2) for m in multipliers()])
请修改multipliers的定义来产生期望的结果
"""
def multipliers():
    return (lambda x:i*x for i in range(4))   # 0,1,2,3
print([m(2) for m in multipliers()])

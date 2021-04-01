#元祖 ：只读列表，可循环查询，可切片。
#      儿子不能改，孙子可能可以改。

tu = (1,2,3,'alex',[2,3,4,'taibai'],'egon')
# 1，索引
print(tu[3])
# 2，切片
print(tu[0:4])
# 3，循环
for i in tu:
    print(i)
# 4,孙子是可变数据类型修改。
tu[4][3]=tu[4][3].upper()
tu[4].append('sb')
print(tu)

# 列表转化成字符串:list -----> str    join
# 字符串转换为列表：str ----->list   split()

li = ['taibai','alex','wusir','egon','女神',]
s = '.'.join(li)
t = s.split('.')
print(s)
print(t)


#range  [1,2,3,4,5,6,.......100........]

# for i in range(3,10):
#     print(i)
# for i in range(10):
#     print(i)
# for i in range(0,10,3):
#     print(i)
# for i in range(10,0,-2):
#     print(i)
# for i in range(10,-1,-2):
#     print(i)

# li = [1,2,3,5,'alex',[2,3,4,5,'taibai'],'afds']
# for i in li:
#     if type(i) == list:
#         for k in i:
#             print(k)
#     else:print(i)

# for i in range(len(li)):
#     if type(li[i]) == list:
#         for j in li[i]:
#             print(j)
#     else:print(li[i])
#
#

# li = [1,2,3,5,'alex',[2,3,4,5,'taibai'],'afds']
# for i in range(len(li)):
#     if  type(li[i]) == list:
#         for j in li[i]:
#             print(j)
#     else:
#         print(li[i])
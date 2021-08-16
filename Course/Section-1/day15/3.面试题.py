
"""
面试题1
1, g是调用生成器函数产生的生成器，一次性产生了多个值的列表。
2, g1对生成器g
"""
def demo():
    for i in range(4):
        yield i


g = demo()
g1 = (i for i in g)
g2 = (i for i in g1)

print(type(g))
print(type(g1))
print(type(g2))
print(list(g))
print(list(g1))
print(list(g2))




# def add(n,i):
#     return n+i
#
# def test():
#     for i in range(4):
#         yield i
#
# g=test()
# for n in [1,10,5]:
#     g=(add(n,i) for i in g)
# # print(list(g))
# # n = 1
# # g=(add(n,i) for i in test())
# # n = 10
# # g=(add(n,i) for i in (add(n,i) for i in test()))
# # n = 5
# # g=(15,16,17,18)
# help(str)
#
# print(list(g))


"""
面试题1
1, g是调用生成器函数产生的生成器，一次性产生了多个值的列表。
2, g1先找g要值，等g2找g1要值的时候，g1已经没有值了。（框里面的鸡蛋被拿光了，别人再来拿就没了）
"""


def demo():
    for i in range(4):
        yield i


g = demo()
g1 = (i for i in g)
g2 = (i for i in g1)

print(list(g))
print(list(g1))
print(list(g2))


"""
面试题2
1,for 循环嵌套生成器表达式，拆开算。
2，生成器表达式和生成器，都不会直接调用，只有真的执行命令的收才会调用。
"""


def add(n, i):
    return n + i

def test():
    for i in range(4):
        yield i

g = test()
for n in [1, 10, 5]:
    g = (add(n, i) for i in g)
print(list(g))
# n=1
# g = (add(n, i) for i in test())
# n=10
# g = (add(n, i) for i in (add(n, i) for i in test()))
# n=5
# g = (add(n, i) for i in (add(n, i) for i in (add(n, i) for i in test())))
# print(list(g))
# n=1
# g = (add(n, i) for i in test())
# n=10
# g = (add(n, i) for i in (add(n, i) for i in test()))
# n=5
# g = (add(n, i) for i in (add(n, i) for i in (add(n, i) for i in [0,1,2,3])))  每个数字加三次5 15，16 17 18
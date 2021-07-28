# 陷阱一：默认参数是一个空的列表
def defult_param(a, l = []):
    l.append(a)
    print(id(l))
    return l

print(defult_param('alex'))
print(defult_param('wuzhibin',l=[]))
print(defult_param('egon'))

# 陷阱二：默认参数是一个空的字典
# def qqxing(k,l = {}):
#     # l.append(1)
#     l[k] = 'v'
#     print(id(l))
#     print(l)
#
# qqxing(1)     #[1]
# qqxing(2,l={})     #[1,l = {}]
# qqxing(3)     #[1,1,1]

# 如果默认参数的值是一个可变数据类型，
# 那么每一次调用函数的时候，
# 如果不传值就公用这个数据类型的资源

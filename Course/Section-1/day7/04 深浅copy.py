
# 一、赋值运算，
# 总结：1，两个列表内存地址一样，所以l1变化了l2也会变化。
#      2，不管属于同一个代码块还是不同代码块，内存地址都是一样的。
l1 = [1,2,3]
l2 = l1
l1.append('a')
print(l1,l2)

# 二、浅copy
#  1，copy的列表，在pycharm同一个文件里面属不同一个代码块，
#  2，浅拷贝后列表内存地址不一样。
#  3,拷贝过后同一个元素的内存地址是一样的。
#  4,如果列表内的元素是不可变数据类型，修改了拷贝的列表，原列表不变。
#  5，如果列表内的元素是可变数据类型，修改了拷贝的列表，原列表要改变。
# 对于浅copy来说，只是在内存中重新创建了开辟了一个空间存放一个新列表，但是新列表中的元素与原列表中的元素是公用的。
# l1 = [1,2,3,[1,2,3]]
# l2 = l1.copy()
# print(l1,l2)
# print(id(l1),id(l2))
# print(id(l1[3]),id(l2[3]))
# eg1:修改列表本身
# l2.append('a')
# print(l1,l2)
# eg2:修改列表中不可变数据类型
# l2[1]=5
# print(l1,l2)
# eg3 修改列表中可变数据类型
# l2[3][1]=5
# print(l1,l2)
#
# l1 = [1,2,[4,5,6],3]
# l2 = l1.copy()

# print(l1,id(l1))
# print(l2,id(l2))
# l1.append('a')
# print(l1,l2)
# l1[2].append('a')
# print(l1,l2)
# print(id(l1[2]))
# print(id(l2[2]))
# 深copy
# 总结：对于深copy来说，列表是在内存中重新创建的，列表中可变的数据类型是重新创建的，列表中的不可变的数据类型是公用的。
import copy
l1 = [1,2,[4,5,6],3]
l2 = copy.deepcopy(l1)
print(l1,id(l1))
print(l2,id(l2))
l1[2].append('a')
print(l1,l2)

# l1 = [1,[1],2,3,4]
# l2 = l1[:]
# l1[1].append('a')
#l2 的结果是什么?


# print(l1,id(l1))
# print(l2,id(l2))
# print(l1[1] is l2[1])

# li = ['alex','taibai','wusir','egon']
# for i in li:
#     print(li.index(i),i)

# for index,i in enumerate(li,1):
#     print(index,i)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: 2019/1/18

from collections import namedtuple
from collections import OrderedDict
from collections import deque
from collections import defaultdict

p = (1,2)
print(type(p))
point = namedtuple('point',['x','y'])
p = point(2,3)
print(p.x)
print(p.y)

circule = namedtuple('s',['x','y','r'])
u = circule(1,3,4)
print(u.x)
print(u.y)
print(u.r)

q = deque(['a','b','c'])
q.append('x')
# print(q)

d = dict([('a',1),['b',2],['c',3]])

print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

od1 = OrderedDict()
od1['x']=1
od1['y']=2
od1['z']=3
print(od1)


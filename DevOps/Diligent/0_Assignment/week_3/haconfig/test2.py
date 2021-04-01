#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu

# a,b,c = 1,2,3
# d = []
# d.extend([a,b,c])
# print(d)
import json

def check_json_format(msg):
    """
    用于判断一个字符串是否符合Json格式
    :param self:
    :return:
    """
    if isinstance(msg, str):  # 首先判断变量是否为字符串
        try:
            json.loads(msg, encoding='utf-8')
        except ValueError:
            return False
        return True
    else:
        return False


# r=input("input")
# ret =check_json_format(r)
# if ret:
#     dic = json.loads(r)
#     print(type(dic))
# else:
#     print(0)

dic = {"name":"alex","age":"19"

}
if type(dic) == dict:
    if "age" in dic.keys():
        print(1)

# if __name__ == "__main__":
#     print(check_json_format("""{"a":1}"""))
#     print(check_json_format("""{'a':1}"""))
#     print(check_json_format({'a': 1}))
#     print (check_json_format(100))
#     print(check_json_format('100'))



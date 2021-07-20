#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2021/7/16

# 1，有变量name = "aleX leNb" 完成如下操作：
name = "aleX leNb"

print(name.strip())  # 去掉两边空格
print(name.lstrip('al')) #
print(name.rstrip("Nb"))
print(name.rstrip("a"))
print(name.strip("ab"))
print(name.startswith("al"))
print(name.endswith("Nb"))
print(name.replace("l","p"))
print(name.replace("l","P",1))
print(name.split("l"))
print(name.split("l",1))
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.count("l"))
print(name.count("l",0,5))
print(name.index("a"))
print(name.index("N"))
print(name.find("a"))
print(name.find("X le"))
print(name[3:7])
print(name[1])
print(name[0:2])
print(name[:3])
print(name[-2:])
print(name[-2:])
print(name.find("e"))

# 2，有字符串s = "123a4b5c"
#
# 1)通过对s切片形成新的字符串s1,s1 = "123"
# 2)通过对s切片形成新的字符串s2,s2 = "a4b"
# 3)通过对s切片形成新的字符串s3,s3 = "1345"
# 4)通过对s切片形成字符串s4,s4 = "2ab"
# 5)通过对s切片形成字符串s5,s5 = "c"
# 6)通过对s切片形成字符串s6,s6 = "ba2"
s = "123a4b5c"
print(s[:3])
print(s[3:6])
print(s[::2])
print(s[1:-2:2])
print(s[-1:])
print(s[-3::-2])

### 3，使用while和for循环分别打印字符串s="asdfer"中每个元素。

s="asdfer"
for i in s:
    print(i)
t=0
while t <len(s):
    print(s[t])
    t +=1

### 4，使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"。

for i in s:
    print(i,end="")
### 5，使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb，    例如：asb, bsb，csb,...gsb
s1="abcdefg"
for i in s1:
    print("sb"+i)
### 6，使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"
s2 ="321"
for i in  s2:
    print("倒计时%s秒！"%i)

### 7，实现一个整数加法计算器(两个数相加)：
#如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。

# content = input("请输入内容:").strip().split("+")
# sum1 =0
# for i in content:
#     j = int(i)
#     sum1 += j
# print(sum1)

### 9，计算用户输入的内容中有几个整数（以个位数为单位）。
#如：content = input("请输入内容：")   # 如fhdal234slfh98769fjdla

# content1 = input("请输入内容：").strip()
# int_count = 0
# for i in content1:
#     if i.isdigit():
#         int_count += 1
# print(int_count)

### 10、写代码，完成下列需求：
# 用户可持续输入（用while循环），用户使用的情况：
# 输入A，则显示走大路回家，然后在让用户进一步选择：
# 是选择公交车，还是步行？
# 选择公交车，显示10分钟到家，并退出整个程序。
# 选择步行，显示20分钟到家，并退出整个程序。
# 输入B，则显示走小路回家，并退出整个程序。
# 输入C，则显示绕道回家，然后在让用户进一步选择：
# # 是选择游戏厅玩会，还是网吧？
# 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
# 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。





### 17、等待⽤户输⼊内容，检测⽤户输⼊内容中是否包含敏感字符？如果存在敏感字符提示“存在敏感字符请重新输⼊”，
# 并允许⽤户重新输⼊并打印。敏感字符：“⼩粉嫩”、“⼤铁锤”
sensitive_check = 1
sensitive_list = ["⼩粉嫩", "⼤铁锤"]
while sensitive_check:
    msg = input("请输入你要输入的信息:").strip()
    for i in sensitive_list:
        if i in msg:
            print("存在敏感字符请重新输⼊")
            break
        else:
            sensitive_check = 0
else:
    print("信息录入成功")












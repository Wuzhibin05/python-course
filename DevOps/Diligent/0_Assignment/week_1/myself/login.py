#!/usr/bin/emv python
# -*- coding:utf-8 -*-
# # small ten

#
import os
import json
if os.path.exists('user.json'):
    print("The file is exist.")
else:
    print("Please check your file.")


file = 'user.json'
fp = open(file, 'r')
user_dict = json.load(fp)  # 将文件中的信息读取到字典中
fp.close()

for key in user_dict:
    for key in user_dict:
        print(key)

file = open('login.txt', 'r')
for line in file:
    Vuser = line.strip().split()[0] #取出文件的中用户名Vuser
    Vpassword = line.strip().split()[1] #取出文件的密码Vpassword
for times in range(10):
    for line in open("times.txt"):
        Vtimes = int(line.strip().split()[0])  # 取出文件的中尝试次数Vtimes
    if Vtimes <= 2:
        if times <= 2:
            print("The remaining attempts is:", remain_atemps)
            username = input("please input username:")
            password = input("please input password:")
            if username == Vuser and password == Vpassword:
                print("welcome")
                break
            else:
                times=times+1
                remain_atemps=remain_atemps-1
                continue
        else:
            Vtimes = str(times)
            open('times.txt', 'w').write(Vtimes)#将Vtime写入的文本times中去
            print("the user is locked")
            break
    else:
        print("The user is locked")
        break
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Wuzhibin
import os
if os.path.exists('user.json'):
    print("The file is exist，please go on!")
    # 判断文件是否存在

    times = 0
    remain_atemps = 3

    file = open('login.txt', 'r')
    for line in file:
        user = line.strip().split()[0]
        # 取出文件的中用户名 user
        passwd = line.strip().split()[1]
        # 取出文件的密码 passwd

    for times in range(10):
        for line in open("login.txt"):
            try_times = int(line.strip().split()[2])
            # 取出文件的中尝试次数try_times

        if try_times <= 2:
            if times <= 2:
                print("The remaining attempts is:", remain_atemps)
                username = input("please input username:")
                password = input("please input password:")

                if username == user and password == passwd:
                    print("welcome")
                    break
                else:
                    times=times+1
                    remain_atemps=remain_atemps-1
                    continue

            else:
                try_times = str(times)
                open('login.txt', 'w').write(try_times)
                '''将Vtime写入的文本times中去'''
                print("the user is locked")
                break

        else:
            print("The user is locked")
            break
else:
    print("Please check your file.")



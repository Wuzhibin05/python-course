#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wuzhibin"
# Email: wuzhibin05@163.com
# Date: 2018/8/20
import os
import json

if os.path.exists("userDetail.json"):
    print("File exists!")
else:
    exit("Can't find any file named userDetail.json!")

with open('userDetail.json', 'r', encoding='utf-8') as f:
    user_dict = json.load(f)

lock_time = 0
remain_time = 3
while True:
    user_option = input("Please input your option:q is quit; l is login;")
    if user_option == 'l':
        user_name = input("Please input username:")
        if user_name in user_dict:
            if user_dict[user_name]["lockTimes"] <= 2:
                user_passwd = input("Please input your password:")

                if user_passwd == user_dict[user_name]["passwd"]:
                    lock_time = 0
                    user_dict[user_name]["lockTime"] = lock_time
                    with open('userDetail.json', 'w', encoding='utf-8') as f:
                        f.write(json.dumps(user_dict))
                    print("Welcome to login on our system!")

                else:
                    lock_time += 1
                    remain_time -= lock_time
                    user_dict[user_name]["lockTime"] = lock_time
                    with open('userDetail.json', 'w', encoding='utf-8') as f:
                        f.write(json.dumps(user_dict))

                    print("Your password is not correct,please check,you only have")
            else:
                exit("You account is locked,Bye bye!")
        else:
            print("Invalid username")
    elif user_option == 'q':
        exit("Welcome to login next time!")
    else:
        print("Invalid input!")

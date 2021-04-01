#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wuzhibin"
# Email: wuzhibin05@163.com
# Date: 2018/5/16
menu = {
    '北京': {
        "昌平": {
            "沙河": ["oldboy", "test"],
            "天通苑": ["链家地产", "我爱我家"]
        },
        "朝阳":{
            "望京": ["奔驰", "陌陌"],
            "国贸": {"CICC", "HP"},
            "东直门": {"Advent", "飞信"},
        },
        "海淀": {},
    },
    '山东': {
        "德州": {},
        "青岛": {},
        "济南": {}
    },
    '广东': {
        "东莞": {},
        "常熟": {},
        "佛山": {},
    },
}

while True:
    for key1 in menu:
        print(key1)
    choice1 = input("choice1>>").strip()
    if choice1 == "b":
        break
    if len(choice1) == 0 or choice1 not in menu:
        continue
    while True:
        for key2 in menu[choice1]:
            print(key2)
        choice2 = input("choice2>>").strip()
        if choice2 == "b":
            break
        if len(choice2) == 0 or choice2 not in menu[choice1]:
            continue

        while True:
            for key3 in menu[choice1][choice2]:
                print(key3)
            choice3 = input("choice3>>").strip()
            if choice3 == "b":
                break
            if len(choice3) == 0 or choice3 not in menu[choice1][choice2]:
                continue

            while True:
                for key4 in menu[choice1][choice2][choice3]:
                    print(key4)
                choice4 = input("choice4>>").strip()
                if choice4 == "b": break
                if len(choice4) == 0 or choice4 not in menu[choice1][choice2][choice3]:
                    continue


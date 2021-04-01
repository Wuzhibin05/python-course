#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wuzhibin"
# Email: wuzhibin05@163.com
# Date: 2018/5/28

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


leve = []
while True:
    for key in menu:
        print(key)
    choice = input("choice>>").strip()

    if choice == "b":
        if len(choice) == 0:
            break
        if len(leve) != 0:
            menu = leve[-1]
            print(leve)
            leve.pop()
        else:
            break

    if len(choice) == 0 or choice not in menu:
        continue
    leve.append(menu)

    # menu
    if menu[choice]:
        menu = menu[choice]  # menu
    else:
        continue





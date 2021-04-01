#!/usr/bin/emv python
# -*- coding:utf-8 -*-
#  Author:small ten
'''
1、if os.path.exists('user.json') and os.path.exists('alex.json') and os.path.exists('wzb.json'):
这里判断的太多了，后面这两个用户的文件没必要判断，因为现在是有两个用户，如果用户上万怎么办，而是后面用到的时候判断，不存在则创建
2、file = 'user.json'
file是关键字，不能用来做变量名或者函数名
另外常量建议用大写区分变量

'''
import json
import os
import time

if os.path.exists('user.json') and os.path.exists('alex.json') and os.path.exists('wzb.json'):
    pass
else:
    print("Please check your file.")  # 不存在则退出程序。
    exit()
    # 判断user.json和shopping.json是否同时存在。同时存在则通过，不同时存在，则提示用户检查文件，退出程序。
file = 'user.json'
fp = open(file, 'r')
user_dict = json.load(fp)
fp.close()
# 打开将json中内容读取到字典user_dict中来，使用完毕关闭文件。

print("-".center(50,"-"))   # 打印相关欢迎语
print("\33[32;1mWelcome to our shopping system,please login in!\033[0m".center(50,"-"))
print("-".center(50,"-"))

for try_times in range(3):
    Username = input("please input  your name:")
    password = input("please input your password:")
    if Username in user_dict:
        user_detail = user_dict[Username]

        if password == user_detail["Password"]:
            print("-".center(50, "-"))
            print("\33[32;1mWelcome to our market mrs %s!\033[0m"%Username)
            print("-".center(50, "-"))
            file = Username+".json"
            file_read =open(file,'r')
            shop_car = json.load(file_read)
            file_read.close()
            break
        else:
            if try_times == 2:
                exit("Too many attempts")
            else:
                print("\33[31;1mThe password is mistake,please try again!!\033[0m")

    else:
        if try_times == 2:
            exit("Too many attempts")
        else:
            print("\33[31;1mThe user is not exists!\033[0m")
'''
上面是用户登录模块。如果用户密码输入正确，则直接进入系统；如果用或者用户名密码连续输错三次（包括用户名输入错误，
可以不是同一个用户），则退出系统。用户需要重新打开程序才能登陆，由于此次作业重点不在这，所以没有做详细的处理。
'''
salary_flag = True
while salary_flag:
    salary = input("Please input your salary :")
    if salary.isdigit():
        salary = int(salary)
        user_dict[Username]["Balance"] += salary
        json.dump(user_dict, open('user.json', 'w'))
        fp.close()  # 打开将json中内容读取到字典user_dict中来，使用完毕关闭文件。
        salary_flag = False

    else:
        print("\33[31;1mInvalid input,please input a number!\033[0m")
print("Your balance is:\33[32;1m%d\033[0m"%(user_detail["Balance"]))
'''
用户输入自己的薪水，如果输入的不符合规定必须重新输入，直到输入对了为止。考虑到输入不合法无法进行下面的操作。
所以这一步强制用户必须输入正确，否则会无限输入。输入的薪水会加上上次的剩余财产一起写入到用户的信息文件中去。
'''

product_read=open('product.json','r')
product_dict =json.load(product_read)
product_read.close()

quit_flag = False  # 退出标志
recharge_flag = True # 充值标志
shop_car_history = {} # 新增购物记录
good_list,good_amount=[],[] # 购物编号记录和购物数量记录购物车
purchases ="" # 所购的所有物品和对应数量字符的拼接

while not quit_flag:
    print("-".center(80, "-"))
    user_action = input("what do you want to do next\33[32;1m[p=purchase,c=check_history,r=recharge,"
                        "q=quit]:\033[0m")
    print("-".center(80, "-"))
    # 提示用户选择自己要做的操作

    if user_action =="q": # 如果输入q直接退出程序
        quit_flag = True

    elif user_action == "p": #如果输入p则购买相关产品
        purchase_flag = True
        Type_flag = True

        while Type_flag:
            ProductType = input("please input the type of goods you want to buy\33[32;1m[M(m)=Phone,F(f)=Food]:\033[0m:")
            if ProductType=="M" or ProductType=="m":
                GoodType = "Phone"
                print("\33[31;1mProduct_dict List\033[0m".center(40, "-"))
                print("NO".center(2), "Name".center(10), "Price".center(6), "Amount".center(3))
                for i in range(10): # 遍历字典按照固定格式输出商品清单
                    if i > 0:
                        No = str(i)
                        if product_dict[No]["Type"] == "Phone":
                            print("%-3s %-10s %-6s %-3s" % (No, product_dict[No]["Goods"], product_dict[No]["Price"],
                                                            product_dict[No]["Number"]))
                    else:
                        pass
                Type_flag = False
                '''输入m或者M打印手机商品列表，按照商品编号输出'''

            elif ProductType=="F" or ProductType=="f":
                GoodType = "Food"
                print("\33[31;1mProduct_dict List\033[0m".center(40, "-"))
                print("NO".center(2), "Name".center(10), "Price".center(6), "Amount".center(3))
                for i in range(10): # 遍历字典按照固定格式输出商品清单
                    if i > 0:
                        No = str(i)
                        if product_dict[No]["Type"] == "Food":
                            print("%-3s %-10s %-6s %-3s" % (No, product_dict[No]["Goods"], product_dict[No]["Price"],
                                                            product_dict[No]["Number"]))
                    else:
                        pass
                Type_flag = False
                '''输入f或者F打印食品商品列表，按照商品编号输出'''
            else:
                print("Invalid input,please try again!")

        while purchase_flag:  # 购物循环程序
            print("-".center(80, "-"))
            good = input("please input number of goods you chose:")  # 用户输入商品的编号
            amount = input("please input amount of goods:")  # 用户输入商品数量
            if good.isdigit() and amount.isdigit():
                # good = int(good)
                amount = int(amount)
                if "0" < good <= "9" and amount < product_dict[good]["Number"] and \
                    product_dict[good]["Type"] == GoodType:
                    good_list.append(good)
                    good_amount.append(amount)
                    shopping_flag = True  # 连续购买标志
                    next = input("what do you want to do next\33[32;1m[p=purchase,e=end,b=back]:\033[0m")
                    '''如果用户输入的商品编号和数量符合购物车内的要求，所输入的商品商品编号必须与选择的商品类型一致。
                    将商品编号和数量存入的对于的列表中，并提示用户做下一步选择。
                    '''

                    while shopping_flag:
                        if next =="p":
                            break
                        elif next == "e":
                            price_total = 0
                            price = 0
                            for i in range(len(good_list)):
                                price = (product_dict[(good_list[i])]["Price"]) * (good_amount[i])
                                price_total += price
                                product_dict[(good_list[i])]["Number"] -=good_amount[i]
                            '''计算本次购物的总额'''

                            if price_total > user_dict[Username]["Balance"]:
                                print("Balance:",user_dict[Username]["Balance"])
                                good_list,good_amount = [],[]
                                print("You balance is not enough,total prices is:",price_total)
                                shopping_flag = False
                                '''如果所购物品总价超过余额，退出本次购物并打印余额'''

                            else:
                                user_dict[Username]["Balance"] -=price_total
                                json.dump(user_dict, open('user.json', 'w'))
                                fp.close()  # 写入余额

                                product_write = open('product.json', 'w')
                                json.dump(product_dict,product_write)
                                product_write.close() #写入购物车信息

                                for i in range(len(good_list)):
                                    purchases =purchases+product_dict[good_list[i]]["Goods"]+','+\
                                               str((good_amount[i]))+";"
                                purchase_time = time.strftime("%Y/%m/%d/%H:%M:%S")
                                shop_car_history[purchase_time] ={}
                                shop_car_history[purchase_time]["goods"]= purchases
                                shop_car_history[purchase_time]["price"] = price_total
                                '''创建购物历史字典shop_car_history'''

                                shop_car.update(shop_car_history)
                                file_write = open(file, 'w')
                                json.dump(shop_car,file_write)
                                file_write.close()
                                '''更新购物车字典，将新的购物车字典写入到对应的用户购物记录文件中去'''

                                print("-".center(50, "-"))
                                print("\33[32;1mThe shopping record as below:\033[0m".center(50, "-"))
                                print("-".center(50, "-"))
                                for key in shop_car_history:
                                    print(key, "Goods and amount:", shop_car_history[key]["goods"], "Total price:",
                                          shop_car_history[key]["price"])
                                print("Balance:",user_dict[Username]["Balance"])
                                '''打印本次购物记录和余额'''

                                good_list, good_amount = [], []
                                shopping_flag = False
                                purchase_flag = False
                                '''退出循环，相关购物参数初始化'''
                        elif next == "b":
                            good_list, good_amount = [], []
                            shopping_flag = False
                            purchase_flag = False
                            '''退出到一级选择，可选择充值、查询、购买退出'''
                        else:
                            print("Invalid input,please try again!")
                            break
                else:
                    print("Not enough amount or the invalid good number,please retry! ")

            else:
                print("Invalid input,please try again!")

    elif user_action == "c":
        start_time = input("please input start_time you chose(like 2016/08/01/00:00:00):")
        end_time = input("please input end_time you chose(like 2016/08/01/00:00:00):")
        if start_time <= end_time:
            print("-".center(50, "-"))
            print("\33[32;1mYour shopping record as below:\033[0m".center(50, "-"))
            print("-".center(50, "-"))
            for key in shop_car:
                if start_time <= key and key <= end_time:
                    print(key,"Goods and amount:",shop_car[key]["goods"],"Total price:",shop_car[key]["price"])
        else:
            print("Invalid input,please try again!")
            '''输入c查询购物，输入开始结束时间，且开始时间必须大于结束时间。'''

    elif user_action == "r":
        while recharge_flag:
            recharge_money = input("How much do you want to recharge:")
            if recharge_money.isdigit():
                recharge_money=int(recharge_money)
                user_dict[Username]["Balance"] +=recharge_money
                json.dump(user_dict, open('user.json', 'w'))
                fp.close()
                print("Your balance is:\33[32;1m%d\033[0m" % (user_detail["Balance"]))
                break
            else:
                print("Invalid input,please try again!")

                '''输入r为账户充值，充值完毕后显示余额并写入用户信息表'''
    else:
        print("Invalid input,please try again!")
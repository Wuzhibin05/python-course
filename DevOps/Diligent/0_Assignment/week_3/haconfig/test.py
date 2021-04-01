# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # Author:Bruce wu
#
import shutil
import os


def fetch(backend):
    """
    查询backend下对应的服务器配置信息，并且写入到fetch_list列表中。
    :param backend:用户输入的backend的信息，例如：www.ordboy.org
    :return:返回查询的的列表内容
    """
    fetch_list = []
    with open('ha.config','r',encoding='utf-8') as  f:

        read_flag = False

        for line in f:
            if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                read_flag = True
                continue
            if read_flag and line.strip().startswith("backend"):
                read_flag = False
                break
            if read_flag and line.strip():
                """
                避免两个避免两个backend信息之间有别的配置信息引起的多读的bug，只有已server开头的才会读取进来，
                遇到新的配置信息则停止读取。
                """
                if line.strip().startswith("server"):
                    fetch_list.append(line.strip())
                else:
                    read_flag = False

    return fetch_list

def add(backend,record):
    """
    增加配置文件中的backend和record信息
    :param backend:接受用户输入的backend信息
    :param record:接受用户输入的record信息
    :return:none
    """

    record_list = fetch(backend)
    print(record_list)
    if not record_list:
        with open('ha.config','r',encoding='utf-8') as old ,open('new.config','w',encoding='utf-8') as new:
            for line in old:
                new.write(line)
            new.write("\nbackend " + backend + "\n")
            new.write(" " * 8 + record + "\n")

    else:
        # backend存在
        if record in record_list:
            shutil.copy("ha.config", 'new.config')
        else:
            # backend存在,record不存在

            '''先将输入的record写入列表中，然后分二种情况去写文件内容:1,对于那么不含有backend和record信息的内容直接写。
            2，对于含有backend信息，但是没有record信息的部分，单独去写入；'''

            record_list.append(record)
            with open('ha.config','r',encoding='utf-8') as old ,open('new.config','w',encoding='utf-8') as new:
                add_flag = False
                for line in old:
                    if line.strip().startswith("backend") and line.strip() == "backend "+backend:
                        new.write(line)
                        add_flag = True
                        for new_line in record_list:
                            new.write(" "*8+new_line+"\n")
                        continue
                    if add_flag and line.strip().startswith("backend"):
                        add_flag = False
                        new.write(line)
                        continue
                    if line.strip() and not add_flag:
                        new.write(line)

def delete(backend,record):
    """
    删除用户输入的record信息和backend信息
    :param backend:接受用户输入的backend信息
    :param record:接受用户输入的record信息
    :return:None
    """
    record_list = fetch(backend)
    # backend不存在
    if not record_list:
        shutil.copy("ha.config", 'new.config')
        print("可删除的record信息为空")
    else:
        # backend存在且不存
        if record  not in record_list:
            shutil.copy("ha.config", 'new.config')
            print("要删除的record信息不存在")
        else:
            delete_flag = False
            record_list.remove(record)

            with open('ha.config','r',encoding='utf-8') as old,open('new.config','w',encoding='utf-8') as new:
                for line in old:
                    if line.strip().startswith('backend') and line.strip() == "backend "+ backend:
                        delete_flag = True
                        '''如果record_list不为空，则写入，如果为空则pass'''
                        if record_list:
                            new.write(line)
                            for new_line in record_list:
                                new.write(' '*8 + new_line + '\n')
                        else:
                            pass
                        continue
                    if delete_flag and line.strip().startswith("backend"):
                        delete_flag = False
                        new.write(line)
                        continue

                    if not delete_flag and line.strip():
                        new.write(line)

def modify(backend,record):
    """
    修改用户输入的record信息
    :param backend: 接受用户输入的backend
    :param record: 接受用户输入的record
    :return: none
    """

    record_list =fetch(backend)
    new_record = []
    lenth =  len(record_list)+1

    if not record_list or record in record_list:
        shutil.copy("ha.config", 'new.config')
    else:
        modify_flag = False
        new_record.append(record)

        with open('ha.config', 'r', encoding='utf-8') as old, open('new.config', 'w', encoding='utf-8') as new:
            for line in old:
                if line.strip().startswith('backend') and line.strip() == "backend " + backend:
                    modify_flag = True
                    '''如果record_list不为空，则写入，如果为空则pass'''
                    new.write("backend "+backend+'\n')
                    for new_line in new_record:
                        new.write(' ' * 8 + new_line + '\n')

                    continue
                if not modify_flag and line.strip():
                    new.write(line)
                if modify_flag:
                    if lenth > 0:
                        lenth -= 1
                        continue
                    else:
                        new.write(line)

def rename():
    """
    重命名ha文件
    :return: none
    """
    if os.path.exists('ha.config') and os.path.exists('new.config'):
        os.renames('ha.config', 'ha.config.bak')
        os.renames('new.config', 'ha.config')
        os.renames('ha.config.bak', 'new.config')
        print('\33[32;1m配置文件已经更新\033[0m')
    else:
        print('文件不存在')


# backend = 'w00.oldboy.org'
# record ='server 10043.1.7.9 1035.1.re.3e we4dht 20 maxconn 3000'
# add(backend,record)
# rename()
#


# li = [11,22]
#
# for i in enumerate(li,1):
#     index = i[0]
#     number = i[1]
#     print(index,number)



def check_json_format(raw_msg):
    """
    用于判断一个字符串是否符合Json格式
    :param self:
    :return:
    """
    if isinstance(raw_msg, str):       # 首先判断变量是否为字符串
        try:
            json.loads(raw_msg, encoding='utf-8')
        except ValueError:
            return False
        return True
    else:
        return False

import json

# s='{"record":{"server1":"100.1.7.9","server2":"100.1.7.9","weight":20,"maxconn":3000}}'
#
# ret=check_json_format(s)
# print(ret)
# dic= json.loads(s) # 将一个字符串，转换成python的基本数据类型; 注意：字符串形式的字典'{"k1":"v1"}'内部的字符串必须是 双引号
# print(type(dic), dic)
# record ='server 100.1.7.d 100.1.d.9we4dht 20 maxconn 3000'
# # r = input("input:")
# # dic = json.loads(r)
# # bk = dic['backend']
# rd = "server %s %s weight %d maxconn %d" %(dic['record']['server1'],
#                                            dic['record']['server2'],
#                                            dic['record']['weight'],
#                                            dic['record']['maxconn'])
#
# print(rd)
# if  dic['record']['server2'] in record or dic['record']['server1'] in record:
#     print(dic['record']['server1'],type(dic['record']['server1']))
#     print(record)
# else:
#     print("不存在的ip")

# dic['record']['server1'] or





# nub='abc'
# num='adecb'
# if nub in mub:
#     print(mub)
# else:
#     print("不存在")
# b='10'
# c=int(b)
# print(type(c))

# ret =num_except(num)
# if ret:
#     pass
# else:
#     print("错误")


# import re
# re.split('; |, ',str)

# a='10.0.0.3'
# # import re
# # # b=re.split('; |, |\*|\n',a)
# # b=re.split('[.][.][.]',a)
# b=a.split(".")
# print(b)

# def ip_split(ip):
#     ip.split(.)

def num_except(num):
    try:
        int(num)
        return int(num)
    except ValueError:
        return 500

def ip_split(ip):
    server1 = ip.split(".")
    server2 = ip.split(".")
    count1=0
    count2=0

    for i in range(len(server1)):

        if 0<= num_except(server1[i]) <=255:
            count1 +=1
        else:
            pass
    for i in range(len(server2)):

        if 0 <= num_except(server2[i]) <= 255:
            count2 += 1
        else:
            pass
    if count1 == len(server1) and count2 ==len(server2):

        return True
    else:
        return False

def user_input():

    json_flag = True
    while json_flag:

        print("json格式的字符串参考信息如下：")
        print('{"record":{"server1":"100.1.7.9","server2":"100.1.7.9","weight":20,"maxconn":3000}}')
        record_json = input("请输入json格式的record信息:")
        json_ret = check_json_format(record_json)
        server_list = []
        if json_ret:
            record_dic = json.loads(record_json)
            num_weight = record_dic['record']['weight']
            num_maxconn = record_dic['record']['weight']
            ip1= record_dic['record']['server1']
            ip2= record_dic['record']['server2']
            if type(record_dic['record']['weight'])== int and type(record_dic['record']['maxconn'])== int\
                    and ip_split(ip1) and ip_split(ip2):


                record = "server %s %s weight %d maxconn %d" % (record_dic['record']['server1'],
                                                                record_dic['record']['server2'],
                                                                record_dic['record']['weight'],
                                                                record_dic['record']['maxconn'])

                server_list.extend([ip1,ip2,record])
                # server_list.append(ip2)
                # server_list.append(record)
                print(server_list)
                json_flag = False

                return server_list

            else:
                print("weight或者maxconn信息输入错误")
        else:
            print("输入的格式不正确，请重新输入")


user_input()


                    #     if num_except(sever1[i]):
        #
        #     # and num_except(server2):
        # print(1)

# a='abcd'
# ip_split(a)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu

import shutil
import os
import json


def num_except(num):
    """
    检查是否为是否可以转换为型
    :param num:接受字符串
    :return:可以转换：数字 不可以转换：返回500
    """
    try:
        int(num)
        return int(num)
    except ValueError:
        return 500


def ip_split(ip):
    """
    判断json中的ip地址是否合法
    :param ip: 接受ip的字符串
    :return: 所有ip都合法:True  其他：返回False
    """
    server1 = ip.split(".")
    server2 = ip.split(".")
    count1 = 0
    count2 = 0

    for i in range(len(server1)):

        if 0 <= num_except(server1[i]) <= 255:
            count1 += 1
        else:
            pass
    for i in range(len(server2)):

        if 0 <= num_except(server2[i]) <= 255:
            count2 += 1
        else:
            pass
    if count1 == len(server1) and count2 == len(server2):
        return True
    else:
        return False

def backup():
    """
    备份ha文件
    :return: none
    """
    if os.path.exists('ha.config') and os.path.exists('ha.bak'):
        shutil.copy('ha.config','ha.bak')
        print('\33[32;1m配置文件已经备份\033[0m')
    else:
        print('文件不存在')

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



def check_json_format(msg):
    """
    用于判断一个字符串是否符合Json格式
    :param msg:接受用户输入的json字符串
    :return:可以转换：返回True 不可以转换：False
    """
    if isinstance(msg, str):       # 首先判断变量是否为字符串
        try:
            json.loads(msg, encoding='utf-8')
        except ValueError:
            return False
        return True
    else:
        return False

def dict_check(dic):
    """
    判断json中的dict信息是否满足record信息的要求
    :param dic: 接受输入的dict信息
    :return: 满足要求：True 不满足：False
    """
    if type(dic) == dict:
        if "record" in dic.keys():
            dic1=dic['record']
            if type(dic1) == dict:
                if "server1" in dic1.keys() and "server2" in dic1.keys() and "weight" in dic1.keys()\
                        and "maxconn" in dic1.keys():
                    value1 = dic1["server1"]
                    value2 = dic1["server2"]
                    value3 = dic1["weight"]
                    value4 = dic1["maxconn"]
                    if type(value1)==str and type(value2)==str and type(value3)==int and\
                        type(value4)==int:
                        return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def user_input():
    """
    接受用户输入的json格式字符串，并进行各项判断和取值。
    :return:返回record
    """
    json_flag = True
    while json_flag:
        global server_list
        server_list = []
        print("*".center(50, '*'))
        print("json格式的字符串参考信息如下：")
        print('{"record":{"server1":"100.1.7.9","server2":"100.1.7.9","weight":20,"maxconn":3000}}')
        print("*".center(50, '*'))
        record_json = input("请输入json格式的record信息:")
        json_ret = check_json_format(record_json)

        if json_ret:
            record_dic = json.loads(record_json)
            dict_ret = dict_check(record_dic)

            if dict_ret:
                ip1 = record_dic['record']['server1']
                ip2 = record_dic['record']['server2']
                if ip_split(ip1) and ip_split(ip2):
                    record = "server %s %s weight %d maxconn %d" % (record_dic['record']['server1'],
                                                                    record_dic['record']['server2'],
                                                                    record_dic['record']['weight'],
                                                                    record_dic['record']['maxconn'])

                    server_list.extend([ip1,ip2,record])
                    json_flag = False
                    return record

                else:
                    print("输入的ip不合法")
            else:
                print("输入的record信息不合法")
        else:
            print("输入的格式不正确，请重新输入")

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
            2，对于含有backend信息，但是没有record信息的部分，单独去写入；3,对于ip已经存在在record中的record，直接调用修改功能'''
            for num in range(len(record_list)):
                if (server_list[0] in record_list[num]) or (server_list[1] in record_list[num]):
                    modify(backend,record_list[num])
                    return True

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

    if server_list[2] in record_list:
        shutil.copy("ha.config", 'new.config')
    else:
        modify_flag = False
        record_list.remove(record)
        record_list.append(server_list[2])

        with open('ha.config', 'r', encoding='utf-8') as old, open('new.config', 'w', encoding='utf-8') as new:
            for line in old:
                if line.strip().startswith('backend') and line.strip() == "backend " + backend:
                    modify_flag = True
                    '''如果record_list不为空，则写入，如果为空则pass'''
                    new.write(line)
                    for new_line in record_list:
                        new.write(' ' * 8 + new_line + '\n')
                    continue
                if modify_flag and line.strip().startswith("backend"):
                    modify_flag = False
                    new.write(line)
                    continue
                if not modify_flag and line.strip():
                    new.write(line)


def main():
    print("-".center(50,'-'))
    print("|",("欢迎来到Ha配置文件修改系统".center(36,' ')),"|")
    print("-".center(50, '-'))
    print("|", ("1，查询backend和sever信息".center(41, ' ')), "|")
    print("|", ("2，添加backend和sever信息".center(41, ' ')), "|")
    print("|", ("3，删除backend和sever信息".center(41, ' ')), "|")
    print("|", ("4，修改backend和sever信息".center(41, ' ')), "|")
    print("|", ("5，备份backend和sever信息".center(41, ' ')), "|")
    print("|", ("6，回滚backend和sever信息".center(41, ' ')), "|")
    print("-".center(50,'-'))
    print("|", (("q:退出;  b：返回上一级   |    操作编号:操作     ").center(31,' ')), "|")
    print("-".center(50, '-'))

    operate_flag = True
    backend_list = ['www.oldboy.org','buy.oldboy.org']
    backend_flag = False
    while operate_flag:
        for items in enumerate(backend_list, 1):
            index = items[0]
            backend_record = items[1]
            print(index,backend_record)
        print("*".center(50, '*'))
        operate_number = input("请输入操作域名编号:")
        print("*".center(50, '*'))

        if operate_number == "1":
            backend = backend_list[0]
            backend_flag = True
        elif operate_number == "2":
            backend = backend_list[1]
            backend_flag = True
        else:
            print("无效的域名编号")


        backup()

        while backend_flag:
            operate_code = input("请参输入对应的操作编号:")
            print("*".center(50, '*'))
            if operate_code == "1":


                ret = fetch(backend)
                if ret:
                    print("查询到的backend信息如下")
                    for item in ret:
                        print(item)
                else:
                    print("\33[32;1m没有相关的配置信息\033[0m")

            elif operate_code == "2":
                ip_config = user_input()
                print("*".center(50, '*'))
                backup()
                add(backend,ip_config)
                rename()
                print("修改后的record信息如下")
                fetch(backend)


            elif operate_code == "3":
                ip_config = user_input()
                print("*".center(50, '*'))
                backup()
                delete(backend,ip_config)
                rename()

            elif operate_code == "4":

                ip_config = user_input()
                print(ip_config)
                backup()
                record_list=fetch(backend)
                if  record_list:
                    for num in range(len(record_list)):
                        if (server_list[0] in record_list[num]) or (server_list[1] in record_list[num]):
                            modify(backend,ip_config)
                            break
                        else:
                            add(backend,ip_config)
                            break
                    rename()
                else:
                    add(backend, ip_config)
                    rename()

            elif operate_code == "5":
                backup()

            elif operate_code == "6":

                if os.path.exists('ha.bak'):
                    os.renames('ha.config', 'ha.config.bak')
                    os.renames('ha.bak', 'ha.config')
                    os.renames('ha.config.bak', 'ha.bak')
                    print('\33[32;1m配置文件已经回滚\033[0m')
                else:
                    print("文件不存在")
            elif operate_code == "b":
                backend_flag = False

            elif operate_code == "q":
                exit("谢谢使用，再见！")

            else:
                print("无效编号，请重试！")
main()






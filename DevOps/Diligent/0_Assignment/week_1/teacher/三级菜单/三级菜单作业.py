#!/usr/bin/emv python
# -*- coding:utf-8 -*-
# small ten


'''
1、需要指出的是
{"爵士乐", "摇滚乐", "世界音乐史"}
这个不是字典，虽然没有报错，但他数据类型并不是字典，
>>> type({"欧洲艺术发展史", "油画","人体素描"})
<class 'set'> ------->这里的类型是集合，不是字典，字典永远的结构是key:value的形式，一定要记住
这样的东西不符合json的语法，所以如果放到json字符串中进行反序列化的话，肯定会报错
2、college_flag = 1 这样的变量最好还是用布尔类型，因为他就两种状态真和假相对于整数类型更节省空间（当然也省不了多少），最关键的是逻辑更清晰

总的来说，这个实现的不错，good job！！

'''
University = {
    "北京大学": {
        "信息技术学院": {"计算机科学":{"计算机原理","数据结构","复变函数","通讯原理"},
                         "信息安全":{"密码学","离散数学"},
                         "云技术":{"大数据基础","数据库原理"}
               },

        "物理学院":{ "电子科学":{"数字电路", "模拟电路","工程光学"},
                     "理论物理":{"量子力学", "半导体物理", "数学物理方法", "天体物理"},
                     "电子信息科学":{"通讯原理", "激光原理", "工程光学", "数字电路"}
                 },
    },
    "清华大学": {
        "外国语学院":{ "英语":{"语言史", "大学英语","专业英语"},
                       "德语":{"德语", "德语基础", "德语发展史"},
                       "韩语":{"韩语", "韩语发展史", "韩语基础", "韩国文化史"}
                 },
        "艺传学院":{ "美术":{"欧洲艺术发展史", "油画","人体素描"},
                     "音乐":{"爵士乐", "摇滚乐", "世界音乐史"}
    }
}
}

print("-------------------------------------------------")
print("Welcome to the specialized query system!".center(50,"*"))
print("-------------------------------------------------")
college_flag = 1  # 一级菜单执行标志等于1.

while college_flag:

    for key in University:  # 遍历university字典打印大学名称
        print(key)
    print("-------------------------------------------------")
    college_name = input("Please input your college（q is quit）:")
    print("-------------------------------------------------")
    academy_flag = 1  # 二级菜单输入标识为置为1.

    if college_name == "q":  # 如果输入q，则退出整个程序。
        college_flag = 0

    elif college_name not in University:  # 如果输入的内容不不符合要求，提示用户重新输入。
        print("please check you college!")

    else:                                   # 如果输入内容是除了q之外的符合要求的菜单，执行下面操作。
        academy_dict = University[college_name]  # 学院选项子字典。

        while academy_flag:

            for key in academy_dict:  # 遍历学院字典，输出学院名称。
                print(key)
            print("-------------------------------------------------")
            academy_name = input("Please input your academy（q is quit and b is back）:")
            print("-------------------------------------------------")
            major_flag = 1  # 三级菜单执行标志置为1.

            if academy_name == "q":  # 如果输入的内容为q，则将一、二级菜单的执行标志置为0.退出循环。
                academy_flag = 0
                college_flag = 0

            elif academy_name == "b":   # 如果输入b，则将二级菜单的执行标志置为0，退回到一级菜单执行。
                academy_flag = 0

            elif academy_name not in academy_dict:  # 如果输入的内容不合法，则提示用户重新输入。
                print("please check you academy!")

            else:                                    # 如果输入的二级菜单的内容在选择之列，进入到三级菜单选择程序。
                major_dict = academy_dict[academy_name]  # 三级菜单选择字字典

                while major_flag:  # 三级菜单执行标志为真，则执行三级菜单。

                    for key in major_dict:  # 遍历三级菜单字典，输入三级菜单内容
                        print(key)
                    print("-------------------------------------------------")
                    major_name = input("Please input your major （q is quit and b is back）:")
                    print("-------------------------------------------------")

                    if major_name in major_dict:  # 如果输入的内容在三级菜单字典中，执行三级菜单子程序。
                        course_flag = 1  # 四级菜单的循环标志置为1.

                        while course_flag:    # 当四级菜单执行标志位真，执行四级循环。
                            course_dict = major_dict[major_name]
                            for key in course_dict:  # 遍历四级菜单子字典，输入菜单内容。
                                print(key)
                            print("-----------------------------------------------------------------------")
                            next_step = input("The query is successful,please make a choice（q is quit and b is back）:")
                            print("----------------------------------------------------------------------- ")

                            if next_step == "q":  # 如果四级菜单中输入了q，则将一、二、三、四级菜单的循环标志都置为0，退出循环。
                                academy_flag = 0
                                college_flag = 0
                                major_flag = 0
                                course_flag = 0
                            elif next_step == "b":  # 如果四级菜单输入了b，则，退出到三级菜单循环。
                                course_flag = 0
                            else:
                                print("Without this option, please enter again!")

                    elif major_name =="q":  # 如果在三级菜单中输入的q，则将一、二、三级菜单的循环标志都置为0，退出循环。
                        academy_flag = 0
                        college_flag = 0
                        major_flag = 0

                    elif major_name =="b":  # 如果输入了b，则退出三级菜单循环，返回二级菜单循环。
                        major_flag = 0
                    else:                    # 如果三级菜单循环中输入的内容不合法，要求用户重新输入。
                        print("please check you major!")
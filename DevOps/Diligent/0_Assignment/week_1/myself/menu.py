#!/usr/bin/emv python
# -*- coding:utf-8 -*-
# small ten
University= {
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
# for i in University:
#     print(i)

# for value in University.values():
#      print(value)
# # for item in University.items():
# #     print(item)
for get_University_name in University.keys():
    # print("获取到的大学名字：%s"%(get_University_name))
    University_name = University[get_University_name]
    for get_college in University_name.keys():
        # print("获取到的学院名称：%s"%get_college)
        college = University_name[get_college]
        for get_major in college.keys():
            # print("获取到的专类类型：%s"%get_major)
            course = college[get_major]
            # print(course[:])
            for get_course in course:
                print("我是%s,%s%s学院的学生，我的学习的课程有:%s。"%(get_University_name,get_college,get_major,get_course))
                # print("我的课程有:",course[:])
    # for ,value in University_name.items():
    #     print('key=%s, value=%s' %(item, value))
# for item,value in University.items():
# print('key=%s, value=%s' %(item, value))
# for item,value in University.items():
#     print('key=%s, value=%s' %(item, value))
# for key in University.keys():
#     University_name=("please input the University name:")
#     if University_name in University_name.keys():
#         for key in  University_name.keys():
#             print(key)
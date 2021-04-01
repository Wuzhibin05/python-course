#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: 2019/2/22

'''
JCBP持续集成脚本
1，通过jenkins拉取代码到本地文件夹。
2，按照指定规范创建文件夹和目录，如果已存在则不创建，不存在则创建。
3，对应用进行关闭操作，如果存在进程则关闭，如果不存在进程则不作操作。
4，判断应用是否发生变化，如果发生变化则备份，如果没有发生变化则不备份。
5，使用更新代码替换运行代码，配置文件替换。备份运行代码按照时间顺序备份。
6，重新启动应用。

'''
import os
src_dir = 'D:\0-jenkins\workspace\185-cspt-jcbp'
work_dir = 'D:\1-Project\CSPT\jcbp'
pro_name = "cspt"
pro_dir = "D:\\Project\\" + pro_name
print(pro_dir)

#def dir_create(**kwargs):

# try:
#     os.path.exists(src_dir) and os.path.exists(work_dir)
# except Exception:
#     print("目录不存在")
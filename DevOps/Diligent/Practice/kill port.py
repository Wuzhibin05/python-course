#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: 2019/3/16

#-*- coding: utf-8 -*-
#!/usr/bin/python
import os
def killport(port):
    # 查找端口的pid
    find_port= 'netstat -aon | findstr 0.0.0.0:%s' % port
    result = os.popen(find_port)
    text = result.read()
    print (text)
    pid= text [-6:-1]
    # 占用端口的pid
    find_kill= 'taskkill -f -pid %s' %pid
    print(find_kill)
    result = os.popen(find_kill)
    return result.read()
killport(7022);
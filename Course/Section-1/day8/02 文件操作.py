# 绝对路径
# f = open('模特主妇护士班主任', mode='r', encoding='UTF-8')
# content = f.read()
# print(content)
# f.close()

# bytes ---->str
# f = open('模特主妇护士班主任', mode='r', encoding='utf-8')
# content = f.read()
# f.write("fjsdlk")
# f.close()

# f = open('模特主妇护士班主任',mode='rb',)
# content = f.read()
# print(content)
# f.close()
# f = open('log',mode='r+',encoding='utf-8')
# print(f.read())
# f.close()

# f = open('log',mode='r+b')
# print(f.read())
# f.write('大猛，小孟'.encode('utf-8'))
# f.close()



# 对于w:没有此文件就会创建文件
# f = open('log',mode='w',encoding='utf-8')
# f.write('骑兵步兵')
# f.close()

# 先将源文件的内容全部清除，在写。
# f = open('log',mode='w',encoding='utf-8')
# f.write('附近看到类似纠纷')
# f.close()


# f = open('log',mode='w+',encoding='utf-8')
# f.write('aaa')
# f.seek(0)
# print(f.read())
# f.close()


# f = open('log',mode='wb')
# f.write('附近看到类似纠纷'.encode('utf-8'))
# f.close()

# f = open('log',mode='a',encoding='utf-8')
# f.write('佳琪')
# f.close()
#
# f = open('log',mode='a',encoding='utf-8')
# f.write('佳琪')
# f.close()



# f = open('log',mode='a+',encoding='utf-8')
# f.write('佳琪')
# f.seek(0)
# print(f.read())
# f.close()


# f = open('log',mode='ab')
# f.write('佳琪'.encode('utf-8'))
# f.close()


# 功能详解
# obj = open('log',mode='r+',encoding='utf-8')
# content = obj.read(3)  # 读出来的都是字符
# obj.seek(3)  # 是按照字节定光标的位置
# obj.tell() # 告诉你光标的位置
# print(obj.tell())
# content = obj.read()
# print(content)
# obj.tell()
# f.readable()  # 是否刻度
# line = f.readline()  # 一行一行的读
# line = f.readlines()  # 每一行当成列表中的一个元素，添加到list中
# f.truncate(4)
# for line in f:
#     print(line)
# f.close()

# f = open('log',mode='a+',encoding='utf-8')
# f.write('佳琪')
# count = f.tell()
# f.seek(count-9)
# print(f.read(2))
# f.close()

# with open('log',mode='r+',encoding='utf-8') as f,\
#         open('log',mode='w+',encoding='utf-8') as f1:


# 文件修改
# 方式一：将硬盘存放的该文件的内容全部加载到内存，在内存中是可以修改的，修改完毕后，再由内存覆盖到硬盘（word，vim，nodpad++等编辑器）
import os  # 调用系统模块

with open('a.txt') as read_f,open('.a.txt.swap','w') as write_f:
    data=read_f.read()  # 全部读入内存,如果文件很大,会很卡
    data=data.replace('alex','SB')  # 在内存中完成修改

    write_f.write(data)  # 一次性写入新文件

os.remove('a.txt')  # 删除原文件
os.rename('.a.txt.swap','a.txt')   # 将新建的文件重命名为原文件

# 方式二：将硬盘存放的该文件的内容一行一行地读入内存，修改完毕就写入新文件，最后用新文件覆盖源文件
import os
with open('a.txt') as read_f,open('.a.txt.swap','w') as write_f:
    for line in read_f:
        line=line.replace('alex','SB')
        write_f.write(line)

os.remove('a.txt')
os.rename('.a.txt.swap','a.txt')

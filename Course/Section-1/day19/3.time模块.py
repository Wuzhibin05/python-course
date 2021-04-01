import time
# time.sleep(100)
# print(time.time())

# 格式化时间  —— 字符串： 给人看的
# 时间戳时间 —— float时间 ： 计算机看的
# 结构化时间 —— 元祖 ：计算用的


# print(time.strftime("%Y-%m-%d %a %H:%M:%S"))  #year month day HOUR MINUTE SECOND
# print(time.strftime("%Y/%m/%d %H:%M:%S"))  #year month day HOUR MINUTE SECOND
# print(time.strftime("%m-%d %H:%M:%S"))  #year month day HOUR MINUTE SECOND
# print(time.strftime("%H:%M:%S"))  #year month day HOUR MINUTE SECOND
# print(time.strftime("%H:%M"))  #year month day HOUR MINUTE SECOND
# print(time.strftime("%Y/%m/%d %a %H:%M:%S"))
# ret = time.localtime()
# print(ret)
# print(type(ret))
# print(time.time())

# struct_time = time.localtime()
# print(struct_time)
# print(struct_time.tm_year)

import time

# 时间戳和结构化时间
ret = time.time()
print(ret)
ret1 = time.localtime(ret)
print(time.gmtime(ret))
print(ret1)
ret2 = time.mktime(ret1)
print(ret2)

# 字符串时间和结构化时间转换。

ret3 = time.localtime()
print(ret3)
ret4 = time.strftime("%Y-%m-%d %H:%M:%S",ret3)
print(ret4)
ret5 =time.strptime(ret4,"%Y-%m-%d %H:%M:%S")
print(ret5)

# 结构化时间转固定格式的字符串时间 %a %b %d %H:%M:%S %Y串

ret6 = time.localtime()
print(time.asctime(ret6))

# 时间戳转换固定格式字符串时间

ret7 = time.time()
print(time.ctime(ret7))





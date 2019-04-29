#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:zhoujinxin
@file: 字符串.py
@time: 2019/04/{DAY}
"""
if __name__ == "__main__":
    pass

# 字符串
str = "zhoujinxin yaoyilin"
print(str[0:])
print(str * 2)
print(str + "Test")
print(str.endswith("in", 0, str.__len__()))
print(str.find("jinxin", 0, len(str)))
print(str.isalnum())    # 都是数字并且至少一个字符
print(str.isalpha())    # 都是字母
print(str.isdigit())    # 都是数字


# %s 格式化字符串
# %c 格式化字符
# %d 格式化整数
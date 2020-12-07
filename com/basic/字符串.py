#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhoujinxin
@file: 字符串.py
@time: 2019/04/{DAY}
"""
if __name__ == "__main__":
    pass

# 字符串
s = "zhoujinxin yaoyilin"
print(len(s))
print(s[0:])
print(s * 2)
print(s + "Test")
print(s.endswith("in", 0, s.__len__()))
print(s.find("jinxin", 0, len(s)))
print(s.isalnum())  # 都是数字并且至少一个字符
print(s.isalpha())  # 都是字母
print(s.isdigit())  # 都是数字

# %s 格式化字符串
# %c 格式化字符
# %d 格式化整数

#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhoujinxin
@file: 正则表达式.py
@time: 2019/05/{DAY}
"""

"""
. 除换行符之外的所有字符
"""

import re

if __name__ == "__main__":
    pass

# str1 = "sshello word"
# regex = r'l'
# match = re.match(regex, str1, re.I)  # 忽略大小写  从句子的开始进行匹配
# if match != None:
#     print("match = ", match.group(0))
# else:
#     print("match is None")
# search = re.search(regex, str1, re.I)  # 允许从句子的中间进行访问  有多个匹配的字串只返回第一个
# if search != None:
#     print("search = ", search.group())
# else:
#     print("search is None")
#
# all = re.findall(regex, str1, re.I) # 返回列表
# print(len(all))

split = re.split(r"\d+", "123gs4") # 按照数字进行切分
print(type(split))
print(split)



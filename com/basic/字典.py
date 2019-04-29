#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:zhoujinxin
@file: 字典.py
@time: 2019/04/{DAY}
"""
if __name__ == "__main__":
    pass


dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code':6734, 'dept': 'sales'}


print(dict['one']) # 输出键为'one' 的值
print(dict[2]) # 输出键为 2 的值
print(tinydict) # 输出完整的字典
print(tinydict.keys()) # 输出所有键
print(tinydict.values()) # 输出所有值
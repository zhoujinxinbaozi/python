#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhoujinxin
@file: 字典.py
@time: 2019/04/{DAY}
"""
if __name__ == "__main__":
    pass

dict = {'one': "This is one", 2: "This is two"}

tinyDict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinyDict)  # 输出完整的字典
print(tinyDict.keys())  # 输出所有键
print(tinyDict.values())  # 输出所有值
print("==========")
for key in tinyDict:
    print("key = %s" % key, end="\t")
    print("value = %s" % tinyDict[key])
for key in dict.keys():
    print("key = %s" % key, end="\t")
    print("value = %s" % dict[key])

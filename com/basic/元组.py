#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhoujinxin
@file: 元组.py
@time: 2019/04/{DAY}
"""
if __name__ == "__main__":
    pass

# 元组 不允许对数据进行更新
tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出第二个至第三个的元素
print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)  # 输出元组两次
print(tuple + tinytuple)  # 打印组合的元组

tup1 = (50,)  # 创建只有一个值的需要有个逗号
for x in tuple:
    print(x, end="\t")

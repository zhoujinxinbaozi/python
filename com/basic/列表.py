#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhoujinxin
@file: 列表.py
@time: 2019/04/{DAY}
"""
if __name__ == "__main__":
    pass

# 列表
listTemp = ['abcd', 786, 2.23, 'john', 70.2]
tinyList = [123, 'john']
print(listTemp)  # 输出完整列表
print(listTemp[0])  # 输出列表的第一个元素
print(listTemp[1:3])  # 输出第二个至第三个的元素
print(listTemp[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinyList * 2)  # 输出列表两次
print(listTemp + tinyList)  # 打印组合的列表
del listTemp[0]  # 删除元素
print(listTemp + tinyList)  # 打印组合的列表

tumple = (123, 123, "周金鑫")
print(list(tumple))  # 元组转列表
print(list.count(list(tumple), 123))  # 123 在列表中出现的次数
list1 = list(tumple)
list1.append("yaoyilin")  # 返回为none  添加元素
print(list1)
list1.pop(-2)  # 删除 默认为最后一个
print(list1)
# list.remove(obj)      移除列表中某个值的第一个匹配项
# list.sort([func])     对原列表进行排序

for i in range(len(list1)):  # list的遍历
    print(list1[i], end="\t")

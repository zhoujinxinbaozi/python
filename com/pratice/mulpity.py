#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:zhoujinxin
@file: mulpity.py
@time: 2019/05/{DAY}
"""
import math

if __name__ == "__main__":
    pass

# 九九乘法表
def mul():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("%d * %d = %d" % (i, j, i * j), end="\t")
        print()

# mul()

def fib(inputStr):
    i1 = 0;
    i2 = 1;
    result = 0
    inputInt = int(inputStr)
    if (inputInt == 1):
        return i1;
    elif (inputInt == 2):
        return i2;
    else:
        for i in range(3, inputInt + 1):
            result = i1 + i2
            i1 = i2
            i2 = result;
        return result

# count = input("需要斐波那契数列的第N项")
# result = fib(count)
# print(result)

#阿姆斯特朗数
#如果一个n位正整数等于其各位数字的n次方之和, 则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。
def am(inputStr):
    inputInt = int(inputStr)
    length = len(inputStr)
    result = 0;
    for i in range(0, length):
        for j in range(i+1, i+2):
            tempInt = int(inputStr[i:j])
            result += math.pow(tempInt, length)
    if result == inputInt:
        return True
    else:
        return False

# count = input("需要判断的数")
# b = am(count)
# print(b)




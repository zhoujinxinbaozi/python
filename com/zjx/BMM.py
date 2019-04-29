#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Burce
@file: BMM.py
@time: 2018/04/{DAY}
"""
#使用逆向最大匹配算法实现中文分词

dic = []

def init():
    """
    读取文件
    获取中文字典
    :return:
    """
    with open("D:/apps/python/8200/dic.txt", "r", encoding="utf-8") as words_dic:
        for word in words_dic:
            dic.append(word.replace("\t","").replace("\n",""))

def if_contain(words):
    """
    判断当前词是否在词典中
    :param words:
    :return:
    """
    flag = False
    for word in dic:
        if word == words:
            flag = True
            break
    return flag

def bmm(sentence):
    """
    逆向最大匹配算法主要实现
    从后往前切割字符串，直到切割出的字符串与字典中的词匹配
    :param sentence:
    :return:
    """
    result = '' #最后返回结果
    words = [] #切词后的结果

    while len(sentence) > 0:
        except_flag = False
        for i in range(len(sentence), 0, -1):
            temp = sentence[:i]
            print("当前句子为 ： " + temp)
            flag = if_contain(temp)
            if flag:
                words.append(temp)
                sentence = sentence[i:]
                print("加入的句子为 ： " + temp)
                except_flag = True
                break
        if not except_flag:
            """
            判断当前字符串是否在字典中并不存在，该字符串从头到尾在字典中都不存在，在直接放入最后结果中
            """
            words.append(sentence)
            print("不存在加入的句子为 ： " + sentence)
            break

    for w in words:
        result += (w + "/")
    return result

def main():
    """
    用户交互接口
    :return:
    """
    init()
    while True:
        input_str = input()
        if not input_str:
            break
        result = bmm(input_str)
        print("BMM分词结果: ")
        print(result)

if __name__ == "__main__":
    main()

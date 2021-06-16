#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 打开文件
print("********-无偏移-****************")
fo = open("kiki.txt", "r")
print ("文件名为: ", fo.name)
 
line = fo.readline()
while line != "":

    print ("读取的数据为: ", line)
    line = fo.readline()
fo.close()

print("*********-设置偏移-*************")
# 重新设置文件读取指针到开头
fo = open("kiki.txt", "r+")
print ("文件名为: ", fo.name)
fo.seek(3,0)
line = fo.readline()
while line != "":

    print ("读取的数据为: ", line)
    line = fo.readline()

 
 
# 关闭文件
fo.close()

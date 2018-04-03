#coding=utf-8
#这个user_info.txt文件要和user_info.py文件放在同一路径下，或者将txt文件以绝对路径的形式写出来；

file = open('user_info.txt','r')
lines = file.readlines()
file.close()

#split中的： 是username和password之间的分割点。split()可以将一个字符串通过通过某个字符为分割点拆分成左右两部分；[0]代表左半部分，[1]代表右半部分；
for line in lines:
    username = line.split(':') [0]
    password = line.split(':') [1]
    print(username,password)
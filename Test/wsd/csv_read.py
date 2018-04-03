#coding=utf-8
#也可以导入xlrd包   即excel的文件包
import csv #导入csv包


#读取本地文件,open()打开后，以reader()读取数据
data = csv.reader(open('info.csv','r'))

#循环输出每一行信息
for user in data:
    print(user)        #每一行数据以数组形式输出
    print(user[2])     #可通过数组下标指定对应数据

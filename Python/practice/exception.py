# #coding=utf-8()
# try:
#     f = open("123.txt")
#     print(f.read())
#     f.close()
# except OSError as reason:
#     print("文件打开出错啦T_T\n 错误原因是：" + str(reason))








# try:
#     sum = 1 + '2'
#     f = open("123.txt")
#     print(f.read())
#     f.close()
#
# except OSError as reason:
#     print("文件打开出错啦T_T\n 错误原因是：" + str(reason))
#
# except TypeError as reason:
#     print("类型出错啦：\n" + str(reason))




try:
    f = open("123.txt")
    print(f.read())
    sum = 1 + '1'

except:
    print("出错啦T_T")

finally:
    f.close()




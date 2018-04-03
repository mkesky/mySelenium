#coding=utf-8
import unittest
from test_case import test_tender
from HTMLTestRunner import HTMLTestRunner
import time
import os

#构造测试集
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    #执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(discover)

    #定义date为日期，time为时间
    date = time.strftime('%Y%m%d')
    time = time.strftime('%Y%m%d%H%M%S')

    #定义path为文件路径，目录级别，可根据实际情况自定义修改
    path = './' + time + '/'

    #定义报告文件路径和名字，路径为前面的path，名字为report（可自定义），格式为.html
    report_path = path + 'report.html'

    #判断是否定义的路径目录存在，不存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass


    with open(report_path,'wb') as report:
        runner = HTMLTestRunner(stream=report_path, title='沃时贷报告', description='投标')
        runner.run(discover)





    '''
    测试结果：
    s
    说明：.代表用例执行通过，两个点表示两个用例执行通过。F表示用例执行不通过。

    '''
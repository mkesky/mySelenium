# coding=utf-8
'''
Created on 2018-03-13
@author: Maco
Project:编写Web测试用例
'''
import unittest
from test_case import test_baidu
from test_case import test_youdao
from HTMLTestRunner import HTMLTestRunner

#构造测试集
# suite = unittest.TestSuite()
# suite.addTest(test_baidu.BaiduTest('test_baidu'))
# suite.addTest(test_youdao.YoudaoTest('test_youdao'))

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(discover)



'''
测试结果：
s
说明：.代表用例执行通过，两个点表示两个用例执行通过。F表示用例执行不通过。

'''
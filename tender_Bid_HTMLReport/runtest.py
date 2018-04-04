import unittest
from test_case import test_tender
from HTMLTestRunner import HTMLTestRunner

#构造测试集
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    #执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(discover)

    f = './' + 'result.html'

    f = open(f,'wb')
    runner = HTMLTestRunner(stream = f,title = '沃时贷报告',description='投标')
    runner.run(discover)




    '''
    测试结果：
    s
    说明：.代表用例执行通过，两个点表示两个用例执行通过。F表示用例执行不通过。

    '''
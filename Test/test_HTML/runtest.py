import unittest,time
from HTMLTestRunner import HTMLTestRunner

#指定测试用例为当前文件夹下的test_case目录
test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    filename = test_dir + '/' + now + 'result.html'
    f = open(filename,'wb')
    runner = HTMLTestRunner(stream=f,
                            title='测试报告',
                            description='用例执行情况:')
    runner.run(discover)
    f.close()

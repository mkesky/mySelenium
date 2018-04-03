# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from HTMLTestRunner import HTMLTestRunner
import time


class woshidai(unittest.TestCase):
    '''沃时贷测试'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.url = "http://dev5.woshidai.com/"
        self.set_window_size(1760, 1040)
        self.verificationErrors = []    #将发生的错误信息，都存放到此列表中；
        self.accept_next_alert = True

    def test_login(self):
        '''沃时贷测试'''
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_css_selector("[href='/common/member/login']").click()
        driver.find_element_by_css_selector("#keywords").send_keys("17855661021")
        driver.find_element_by_css_selector("#password").send_keys("wo1111")
        driver.find_element_by_css_selector("[type='submit']").submit()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(woshidai("test_login"))

    #按照一定格式获取当前时间
    now = time.strftime("%Y_%m_%d %H:%M:%S")

    #定义报告存放路径
    filename = './' + now + '_' + 'result.html'
    f = open(filename,'wb')    #通过open()方法，以二进制 “写” 模式打开当前目录下的result.html,如果没有，则自动创建该文件；

    #定义测试报告： stream指定测试报告文件； title用于定义测试报告的标题； description用于定义测试报告的副标题；
    runner = HTMLTestRunner(stream = f,
                            title = "百度搜索测试报告",
                            description = "用例执行情况："
    )
    #通过HTMLTestRunner中的run()方法来运行测试套件中的测试用例；
    runner.run(suite)  #运行测试用例
    #运行完成后，一定要记得关闭文件；
    f.close()

#Python自动化测试--一个简单的自动化测试脚本--批量执行测试用例
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common import exceptions
import unittest,time,re

class Baidu(unittest.TestCase):
    #setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。这里将浏览器的调用和URL的访问放到初始化部分。#
    def setUp(self): 
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url='http://www.baidu.com/'
        self.verificationErrors=[]  #脚本运行时，错误的信息将被打印到这个列表中#
        self.accept_next_alert=True  #是否继续接受下一个警告#

    #百度搜索用例
    def test_baidu_serch(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys(u"沃时贷")
        driver.find_element_by_id("su").click()
        driver.quit()
        time.sleep(5)

    #百度设置用例
    def test_baidu_set(self):
        driver=self.driver
        #进入搜索设置页
        driver.get(self.base_url)
        above = driver.find_element_by_link_text(u"设置")
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_link_text("搜索设置").click()
        sel = driver.find_element_by_css_selector("#nr")
        Select(sel).select_by_visible_text(u"每页显示50条")
        driver.find_element_by_link_text("保存设置").click()
        driver.switch_to_alert().accept()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
        '''
        tearDown 方法在每个测试方法执行后调用，这个地方做所有清理工作，如退出浏览器等。 
        self.assertEqual([], self.verificationErrors) 是个难点，
        对前面verificationErrors方法获得的列表进行比较；如查verificationErrors的列表不为空，输出列表中的报错信息。'''
if __name__=="__main__":
    unittest.main() #执行用例#
 
'''
执行结果如下：
Ran 2 tests in 30.719s  执行测试完所有测试用例，用了70.719S
 
ok 没有问题
 
如果你在用例中故意设置一个错误，例如：
百度设置用例中增加这样一行代码，查找到name为DR的标签，并单击它，因为这个是没有的，找不到这个标签，系统会报错，
driver.find_element_by_name('DR').click()
这时执行结果显示如下：
Ran 2 tests in 70.719s
 
FAILED (errors=1)
'''

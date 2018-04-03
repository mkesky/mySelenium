#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import *
import unittest,re,os
import time
import HTMLTestRunner


class baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(5)

    def test_search(self):
        driver = self.driver
        # driver.find_element_by_css_selector("input#q").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"张三丰")
        driver.find_element_by_css_selector("[type='submit']").click()
        sleep(2)
        test1 = driver.find_element_by_xpath(".//*[@id='mainsrp-related']/div/dl/dd/a[2]").text
        # 此处的xpath是注册时手机号一栏的xpath
        print(test1)
        try:
            self.asserEqual(test1, u"太极张三丰", u"搜索失败")
        except:
            driver.get_screenshot_as_file("E:\img\search.jpg")
        sleep(5)


if __name__ == '__main__':
      today = time.strftime('%Y%m%d%H%m%S', time.localtime(time.time()))
      suite = unittest.TestSuite()
      suite.addTest(baidu("test_search"))
      reportPath = "E:/img/report/" + today + ".html"
      fp = open(reportPath, 'wb')
      runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                             title='Python Test Report',
                                             description='This  is Python  Report')
      runner.run(suite)

      runner.close()



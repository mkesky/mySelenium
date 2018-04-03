# coding=utf-8
'''
Created on 2018-03-13
@author: Maco
Project:编写Web测试用例
'''
from selenium import webdriver
import unittest, time


class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)  # 隐性等待时间为10秒
        self.url = "https://www.baidu.com"

    def test_baidu(self):
        driver = self.driver
        driver.get(self.url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"沃时贷")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        title = driver.title
        self.assertEqual(title, u"沃时贷_百度搜索")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
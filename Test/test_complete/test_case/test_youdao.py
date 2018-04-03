# coding=utf-8
'''
Created on 2018-03-13
@author: Maco
Project:编写Web测试用例
'''
from selenium import webdriver
import unittest, time


class YoudaoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)  # 隐性等待时间为10秒
        self.url = "http://www.youdao.com"

    def test_youdao(self):
        driver = self.driver
        driver.get(self.url + "/")
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys(u"你好")
        driver.find_element_by_id("translateContent").submit()
        time.sleep(3)
        page_source = driver.page_source
        self.assertIn("hello", page_source)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
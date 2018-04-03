from selenium import webdriver
import unittest
from time import *

class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_baidu(self):
        driver = self.driver
        driver.get("https://www.baidu.com/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("沃时贷")
        driver.find_element_by_css_selector("[type='submit']").click()
        sleep(3)
        title = driver.title
        self.assertEqual(title,"沃时贷_百度搜索")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
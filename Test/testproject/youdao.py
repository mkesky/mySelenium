from selenium import webdriver
from time import *
import unittest

class TestYoudao(unittest.TestCase):

    def setUp(self):
        driver = self.driver
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)

    def test_youdao(self):
        driver = self.driver
        driver.get("http://dict.youdao.com/")
        driver.find_element_by_css_selector("#translateContent").clear()
        driver.find_element_by_css_selector("#translateContent").send_keys("美女")
        driver.find_element_by_link_text("翻译").click()
        sleep(3)
        title = driver.title
        self.assertEqual(title,"美女_有道搜索")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

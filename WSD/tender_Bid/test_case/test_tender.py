#coding=utf-8
from selenium import webdriver
import unittest,time

class BidTest(unittest.TestCase):
    '''沃时贷测试报告'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.url = 'https://devs.woshidai.com/'

    def test_tender(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.url)
        driver.find_element_by_link_text('登录').click()
        driver.find_element_by_id('keywords').clear()
        driver.find_element_by_id('keywords').send_keys("19955880001")
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(u"wo1111")
        driver.find_element_by_css_selector("[type=submit]").click()
        time.sleep(5)
        driver.find_element_by_link_text("我要投资").click()
        time.sleep(3)
        driver.find_element_by_css_selector('[title=lei005]').click()
        time.sleep(3)
        driver.find_element_by_name("money").send_keys("100")
        #driver.find_element_by_css_selector('[href=javascript:void(0)]').click()      全部投入
        driver.find_element_by_css_selector(".tender-sub").click()
        time.sleep(3)
        driver.find_element_by_css_selector("#J-payPwdBANK").send_keys("test5566")
        driver.find_element_by_css_selector('[type=submit]').click()
        time.sleep(5)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
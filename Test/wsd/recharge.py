from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import *
from public import Login
import unittest

class TestRecharge(unittest.TestCase):
    def setUp(self):
        print("开始充值")

    def tearDown(self):
        print("充值结束")

    def test_recharge(self):
        driver = self.driver
        Login().login()

        # 进行充值
        driver.find_element_by_css_selector(".btn-charge").click()
        driver.find_element_by_xpath("//input[@name='amount']").send_keys("997.32")

        # 用键盘的ENTER键代替鼠标的click事件
        driver.find_element_by_css_selector("[type='submit']").send_keys(Keys.ENTER)

        # 接受alert
        driver.switch_to_alert().accept()

        driver.find_element_by_link_text("发送验证码").click()
        driver.switch_to_alert().accept()
        driver.find_element_by_css_selector("[match='smsCode']").send_keys("666666")
        driver.find_element_by_link_text("确认充值").click()
        driver.find_element_by_link_text("立即跳转").click()

        print(ctime())


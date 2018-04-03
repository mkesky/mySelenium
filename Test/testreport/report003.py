from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import *
import unittest
from HTMLTestRunner import HTMLTestRunner

class woshidai(unittest.TestCase):
    '''沃时贷测试'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.url = "https://dev5.woshidai.com/"
        #设置浏览器窗口大小
        self.driver.set_window_size(1920,1042)

    def test_recharge(self):
        '''登录后进行充值'''
        driver = self.driver
        driver.get(self.url)
        # driver.maximize_window()
        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_css_selector("#keywords").send_keys("lau2xs")
        driver.find_element_by_css_selector("[type='password']").send_keys("wo1111")
        driver.find_element_by_css_selector(".btn").submit()
        sleep(5)

        #进入充值阶段
        driver.find_element_by_css_selector(".btn-charge").click()
        #输入要充值的金额
        driver.find_element_by_xpath("//input[@name='amount']").send_keys("50000")
        #用键盘的ENTER键代替鼠标的click事件
        driver.find_element_by_css_selector("[type='submit']").send_keys(Keys.ENTER)
        #接受alert
        sleep(3)
        driver.switch_to_alert().accept()
        sleep(5)
        driver.find_element_by_link_text("发送验证码").click()
        driver.switch_to_alert().accept()
        sleep(3)
        driver.find_element_by_css_selector("[match='smsCode']").send_keys("666666")
        driver.find_element_by_link_text("确认充值").click()
        driver.find_element_by_link_text("立即跳转").click()
        driver.find_element_by_css_selector(".a-link1").click()
        sleep(8)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(woshidai("test_recharge"))

    #按照一定格式获取当前时间
    # now = time.strftime("%Y%m%d_%H%M%S")
    # 将当前时间加入到报告文件名称中
    f = './' + 'result.html'

    f = open(f,'wb')

    runner = HTMLTestRunner(stream=f,title="沃时贷测试报告",description="用例执行情况")
    runner.run(suite)
    f.close()
















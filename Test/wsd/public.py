from selenium   import webdriver
from time import *


#建立公共类
class Login:
    def __init__(self):
        driver = self.webdriver.Firefox()
        driver.get("https://dev5.woshidai.com/")
        driver.set_window_size(1680, 1039)
        driver.implicitly_wait(5)
        print(driver.title)

#登录
    def login(self):
        driver = self.driver
        driver.find_element_by_link_text("登录").click()
        sleep(3)
        driver.find_element_by_css_selector("#keywords").send_keys("17855661015")
        driver.find_element_by_css_selector("[type='password']").send_keys("wo1111")
        driver.find_element_by_css_selector(".btn").submit()
        sleep(3)

#退出
    def logout(self):
        print("退出沃时贷")


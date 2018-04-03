# from selenium import webdriver
# from time import *

#数据驱动模型

class Login():

    #登录
    def user_login(self,driver,username,password):
        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_css_selector("#keywords").send_keys(username)
        driver.find_element_by_css_selector("[type='password']").send_keys(password)
        driver.find_element_by_css_selector(".btn").submit()



    def user_logout(self,driver):
        driver.find_element_by_link_text("退出").click()
        driver.quit()


#coding=utf-8
from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
from time import *
from pp import Login


driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("https://dev5.woshidai.com/")

#调用登录模块
Login().user_login(driver)
print(driver.title)





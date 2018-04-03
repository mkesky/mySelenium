#coding=utf-8
from selenium import webdriver
from time import *

driver = webdriver.Firefox()
driver.get("https://dev5.woshidai.com/")
sleep(5)

print(driver.title)

#截取当前窗口，并指定截图图片的保存位置
driver.get_screenshot_as_file("E:\img\wsd.jpg")

# driver.find_element_by_id("kw").send_keys("NBA")
# driver.find_element_by_id("su").submit()
#
# sleep(5)






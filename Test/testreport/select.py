#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import *

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get('http://www.baidu.com')

above = driver.find_element_by_link_text(u"设置")
ActionChains(driver).move_to_element(above).perform()

driver.find_element_by_link_text("搜索设置").click()
sel = driver.find_element_by_css_selector("#nr")
Select(sel).select_by_value('50')
driver.find_element_by_css_selector(".prefpanelgo").click()
text = driver.find_element_by_css_selector(".prefpanelgo").text
print(text)
print(ctime())

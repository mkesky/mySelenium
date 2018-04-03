#coding=utf-8
from selenium import webdriver
#调用ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import os
driver = webdriver.Firefox ()
driver.maximize_window()
driver.get("https://www.taobao.com/")
driver.find_element_by_link_text("免费注册").click()
sleep(5)

driver.find_element_by_xpath(".//*[@id='J_AgreementBtn']").click()
driver.find_element_by_css_selector("#J_Mobile").send_keys("17755661100")
sleep(5)

for i in range(2):
    element = driver.find_element_by_id("nc_1_n1z")
    ActionChains(driver).drag_and_drop_by_offset(element,300,0).perform()
    driver.find_element_by_link_text("刷新").click()
    sleep(2)
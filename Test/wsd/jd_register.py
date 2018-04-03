#coding=utf-8
from selenium import webdriver
from time import *
import os
# IEDriverServer=os.path.abspath(r"C:\Program Files\Internet Explorer\IEDriverServer.exe")
# os.environ['webserver.ie.driver']=IEDriverServer
driver = webdriver.Firefox()
sleep(2)
driver.maximize_window()
driver.get("https://www.jd.com/")
sleep(2)
driver.find_element_by_link_text("免费注册").click()

# driver.find_element_by_xpath(".//*[@id='form-account']").click()

#/*xpath的路径以button的xpath路径前面的内容为准，这样更精确，先点击“同意协议”找到其xpath中button前面的路径
div = driver.find_element_by_xpath("html/body/div[4]/div[2]/div/div[2]").find_element_by_tag_name("button")
div.click()
sleep(5)
driver.find_element_by_css_selector("input#form-account").send_keys("Williamxx1")
sleep(2)
driver.find_element_by_xpath(".//*[@id='register-form']/div[3]/txt").click()
sleep(2)
driver.find_element_by_css_selector("input[id='form-pwd']").send_keys("William123")
sleep(2)
driver.find_element_by_xpath(".//*[@id='register-form']/div[5]/txt").click()
sleep(2)
driver.find_element_by_id("form-equalTopwd").send_keys("William123")
sleep(2)
driver.find_element_by_xpath(".//*[@id='register-form']/div[8]/div[1]/txt").click()
sleep(2)
driver.find_element_by_id("form-phone").send_keys("15655791897")
sleep(2)
driver.quit()
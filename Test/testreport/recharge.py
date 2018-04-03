from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import *

driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get("https://dev5.woshidai.com/")
driver.set_window_size(1680,1039)
sleep(3)

print(driver.title)

#登录用户
driver.find_element_by_link_text("登录").click()
sleep(3)
driver.find_element_by_css_selector("#keywords").send_keys(u"雪舞漫天")
driver.find_element_by_css_selector("[type='password']").send_keys("wo1111")
driver.find_element_by_css_selector(".btn").submit()
sleep(3)

# #接受托管合作协议
# driver.find_element_by_css_selector(".layui-layer-btn0").click()
# driver.find_element_by_css_selector("[type='submit']").click()
# #接受alert
# driver.switch_to_alert().accept()







# #进行充值
# driver.find_element_by_css_selector(".btn-charge").click()
# driver.find_element_by_xpath("//input[@name='amount']").send_keys("30000")
# #用键盘的ENTER键代替鼠标的click事件
# driver.find_element_by_css_selector("[type='submit']").send_keys(Keys.ENTER)
# #接受alert
# driver.switch_to_alert().accept()
#
# driver.find_element_by_link_text("发送验证码").click()
# driver.switch_to_alert().accept()
# driver.find_element_by_css_selector("[match='smsCode']").send_keys("666666")
# driver.find_element_by_link_text("确认充值").click()
# driver.find_element_by_link_text("立即跳转").click()
#
# print(ctime())







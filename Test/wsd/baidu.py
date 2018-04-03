from selenium import webdriver

#参数化搜索关键字

#创建一个数组，将搜索的关键字存放进来，通过for循环遍历数组，最后把遍历的数组元素作为每次百度搜索的关键字
search_text = ['python','中文','text']

for text in search_text:
    driver =webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get("https://www.baidu.com/")
    driver.find_element_by_id("kw").send_keys(text)
    driver.find_element_by_id("su").click()
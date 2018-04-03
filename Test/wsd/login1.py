from selenium import webdriver
from time import *
from pp1 import Login

class LoginTest():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("https://dev5.woshidai.com/")

    #用户登录
    def test_login(self):
        username = '17855661015'
        password = 'wo1111'
        Login().user_login(self,driver,username,password)

LoginTest().test_login()
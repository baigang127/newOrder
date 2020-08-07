from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.support import select
from selenium.common import exceptions
import unittest,time,re
class Baidueee(unittest.TestCase):
    #setUp 用于设置初始化的部分，在测试用例执行前，这个方法的函数将会被提前调用
    def test_ccc(self):
        self.driver = webdriver.Chrome()#self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)#self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accapt_next_alert = True
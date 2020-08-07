from idlelib import browser
from time import sleep

import trio
import unittest
from selenium .webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class MyTestCase(unittest.TestCase):
     def test_something(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://jxtest.eins2eins.com/index.html")


        self.driver.find_element_by_name("orgName").send_keys("杭州龙伯科技有限公司")

        self.driver.find_element_by_name("username").send_keys("testjx")

        self.driver.find_element_by_name("password").send_keys("123456")

        self.driver.find_element_by_xpath("//*[@id='account_from']/div[5]/button").click()
        locator=self.driver.find_element_by_xpath("//*[@id='side-menu']/li[1]/div[1]/h3").text
        text=u"壹二壹"
        result=EC.text_to_be_present_in_element(locator,text)
        #print (result)
        if locator==text:
           print("登录成功啦")
        else:
           print("登录失败了，呜呜呜")
        ##点击订单操作
        self.driver.find_element_by_xpath("//*[@id='side-menu']/li[3]/a/span[1]").click()
        ##打开订单录入
        self.driver.find_element_by_xpath("//*[@id='side-menu']/li[3]/div/div/div[2]/div[2]/a[2]").click()

        iframe = self.driver.find_element_by_xpath("//iframe[@name='iframe4']")
        self.driver.switch_to.frame(iframe)
        sleep(3)
        # 点击录入按钮
        self.driver.find_element_by_xpath("//div[@class='btnStyle']").click()
        #self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[1]/a[2]").click()
        sleep(3)
        Select(self.driver.find_element_by_id("ShopName")).select_by_visible_text(u"售后换货店铺")
        self.driver.find_element_by_id("ShopName").click()
        self.driver.find_element_by_id("sourceBillNo").click()
        self.driver.find_element_by_id("sourceBillNo").click()
        self.driver.find_element_by_id("sourceBillNo").clear()
        self.driver.find_element_by_id("sourceBillNo").send_keys("bg-se123456789")
        self.driver.find_element_by_name("payType").click()
        Select(self.driver.find_element_by_name("payType")).select_by_visible_text(u"支付宝")
        self.driver.find_element_by_name("payType").click()
        self.driver.find_element_by_name("customerName").click()
        self.driver.find_element_by_name("clientPhone").click()
        self.driver.find_element_by_name("receiverName").click()
        self.driver.find_element_by_name("customerName").click()
        self.driver.find_element_by_name("customerName").clear()
        self.driver.find_element_by_name("customerName").send_keys(u"慕白")
        self.driver.find_element_by_name("clientPhone").click()
        self.driver.find_element_by_name("clientPhone").click()
        self.driver.find_element_by_name("clientPhone").clear()
        self.driver.find_element_by_name("clientPhone").send_keys("18868026855")
        self.driver.find_element_by_name("receiverName").click()
        self.driver.find_element_by_name("receiverName").clear()
        self.driver.find_element_by_name("receiverName").send_keys(u"月月")
        self.driver.find_element_by_name("receiverMobile").click()
        self.driver.find_element_by_name("receiverMobile").clear()
        self.driver.find_element_by_name("receiverMobile").send_keys("18268026852")
        self.driver.find_element_by_id("receiverPhone").click()
        self.driver.find_element_by_id("receiverPhone").clear()
        self.driver.find_element_by_id("receiverPhone").send_keys("05718956421")
        self.driver.find_element_by_xpath("//form[@id='shop_form']/div/div/div[2]/div[10]/div/div/div/span").click()
        self.driver.find_element_by_xpath("//form[@id='shop_form']/div/div/div[2]/div[10]/div/div/ul/li[3]").click()
        self.driver.find_element_by_xpath("//form[@id='shop_form']/div/div/div[2]/div[10]/div/div/ul/li[2]").click()
        self.driver.find_element_by_xpath("//form[@id='shop_form']/div/div/div[2]/div[10]/div/div/ul/li[2]").click()
        self.driver.find_element_by_name("receiverAddress").click()
        self.driver.find_element_by_name("receiverAddress").clear()
        self.driver.find_element_by_name("receiverAddress").send_keys(u"杭州逗包自动化测试部")
        self.driver.find_element_by_xpath("//form[@id='shop_form']/div/div[2]/div/div[2]/a/div/i").click()
        self.driver.find_element_by_id("jqg_ItemListPop_table_1260167249195089921").click()
        self.driver.find_element_by_id("jqg_ItemListPop_table_1260165416934359041").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        self.driver.find_element_by_name("eoOrderLineList[0].qty").click()
        self.driver.find_element_by_name("eoOrderLineList[0].qty").clear()
        self.driver.find_element_by_name("eoOrderLineList[0].qty").send_keys("10")
        self.driver.find_element_by_name("eoOrderLineList[0].itemPrice").click()
        self.driver.find_element_by_name("eoOrderLineList[0].itemPrice").clear()
        self.driver.find_element_by_name("eoOrderLineList[0].itemPrice").send_keys("3000")
        self.driver.find_element_by_name("eoOrderLineList[1].itemPrice").click()
        self.driver.find_element_by_name("eoOrderLineList[1].itemPrice").clear()
        self.driver.find_element_by_name("eoOrderLineList[1].itemPrice").send_keys("3000")
        self.driver.find_element_by_name("eoOrderLineList[1].qty").click()
        self.driver.find_element_by_name("eoOrderLineList[1].qty").clear()
        self.driver.find_element_by_name("eoOrderLineList[1].qty").send_keys("30")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        self.driver.find_element_by_xpath("//div[@id='TipsPop']/div[3]/div/div/a").click()
        self.driver.find_element_by_xpath("//form[@id='shop_form']/div/div[2]/div/div/h3").click()
        self.driver.find_element_by_name("buyerNick").click()
        self.driver.find_element_by_name("eoOrderLineList[1].itemPrice").click()
        self.driver.find_element_by_name("eoOrderLineList[1].itemPrice").clear()
        self.driver.find_element_by_name("eoOrderLineList[1].itemPrice").send_keys("2000")




if __name__ == '__main__':
    unittest.main()

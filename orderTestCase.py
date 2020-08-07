
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium import webdriver


class OrderTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://jxtest.eins2eins.com/index.html"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_order_test_case(self):
        driver = self.driver
        driver.get("https://jxtest.eins2eins.com/index.html")
        driver.find_element_by_link_text(u"线下订单").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_xpath("//div[2]/div/div/div").click()
        driver.find_element_by_xpath("//a[2]/div/div").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=2 | ]]
        driver.find_element_by_id("ShopName").click()
        Select(driver.find_element_by_id("ShopName")).select_by_visible_text(u"奥服京东供货商")
        driver.find_element_by_id("ShopName").click()
        driver.find_element_by_id("sourceBillNo").click()
        driver.find_element_by_id("sourceBillNo").click()
        driver.find_element_by_id("sourceBillNo").clear()
        driver.find_element_by_id("sourceBillNo").send_keys("bg-se123456789")
        driver.find_element_by_name("payType").click()
        Select(driver.find_element_by_name("payType")).select_by_visible_text(u"支付宝")
        driver.find_element_by_name("payType").click()
        driver.find_element_by_name("customerName").click()
        driver.find_element_by_name("clientPhone").click()
        driver.find_element_by_name("receiverName").click()
        driver.find_element_by_name("customerName").click()
        driver.find_element_by_name("customerName").clear()
        driver.find_element_by_name("customerName").send_keys(u"慕白")
        driver.find_element_by_name("clientPhone").click()
        driver.find_element_by_name("clientPhone").click()
        driver.find_element_by_name("clientPhone").clear()
        driver.find_element_by_name("clientPhone").send_keys("18868026855")
        driver.find_element_by_name("receiverName").click()
        driver.find_element_by_name("receiverName").clear()
        driver.find_element_by_name("receiverName").send_keys(u"月月")
        driver.find_element_by_name("receiverMobile").click()
        driver.find_element_by_name("receiverMobile").clear()
        driver.find_element_by_name("receiverMobile").send_keys("18268026852")
        driver.find_element_by_id("receiverPhone").click()
        driver.find_element_by_id("receiverPhone").clear()
        driver.find_element_by_id("receiverPhone").send_keys("05718956421")
        driver.find_element_by_xpath("//form[@id='shop_form']/div/div/div[2]/div[10]/div/div/div/span").click()
        driver.find_element_by_xpath("//form[@id='shop_form']/div/div/div[2]/div[10]/div/div/ul/li[3]").click()
        driver.find_element_by_xpath("//form[@id='shop_form']/div/div/div[2]/div[10]/div/div/ul/li[2]").click()
        driver.find_element_by_xpath("//form[@id='shop_form']/div/div/div[2]/div[10]/div/div/ul/li[2]").click()
        driver.find_element_by_name("receiverAddress").click()
        driver.find_element_by_name("receiverAddress").clear()
        driver.find_element_by_name("receiverAddress").send_keys(u"杭州逗包自动化测试部")
        driver.find_element_by_xpath("//form[@id='shop_form']/div/div[2]/div/div[2]/a/div/i").click()
        driver.find_element_by_id("jqg_ItemListPop_table_1260167249195089921").click()
        driver.find_element_by_id("jqg_ItemListPop_table_1260165416934359041").click()
        driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        driver.find_element_by_name("eoOrderLineList[0].qty").click()
        driver.find_element_by_name("eoOrderLineList[0].qty").clear()
        driver.find_element_by_name("eoOrderLineList[0].qty").send_keys("10")
        driver.find_element_by_name("eoOrderLineList[0].itemPrice").click()
        driver.find_element_by_name("eoOrderLineList[0].itemPrice").clear()
        driver.find_element_by_name("eoOrderLineList[0].itemPrice").send_keys("3000")
        driver.find_element_by_name("eoOrderLineList[1].itemPrice").click()
        driver.find_element_by_name("eoOrderLineList[1].itemPrice").clear()
        driver.find_element_by_name("eoOrderLineList[1].itemPrice").send_keys("3000")
        driver.find_element_by_name("eoOrderLineList[1].qty").click()
        driver.find_element_by_name("eoOrderLineList[1].qty").clear()
        driver.find_element_by_name("eoOrderLineList[1].qty").send_keys("30")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//div[@id='TipsPop']/div[3]/div/div/a").click()
        driver.find_element_by_xpath("//form[@id='shop_form']/div/div[2]/div/div/h3").click()
        driver.find_element_by_name("buyerNick").click()
        driver.find_element_by_name("eoOrderLineList[1].itemPrice").click()
        driver.find_element_by_name("eoOrderLineList[1].itemPrice").clear()
        driver.find_element_by_name("eoOrderLineList[1].itemPrice").send_keys("2000")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
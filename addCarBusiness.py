# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import unittest


class SeleniumIde1(unittest.TestCase):

    # 准备环节
    def setUp(self):
        # 启动火狐浏览器并且获得实例对象
        self.driver = webdriver.Firefox()
        # 测试地址
        self.base_url = "http://oatest.bujidele.com:48081/"

    # 开始
    def test_start(self):
        # 实例
        driver = self.driver

        # 登录
        driver.get(self.base_url + "/Admin/Account/Login")
        driver.find_element_by_id("USER_ID").send_keys("linxue")
        driver.find_element_by_id("PASSWORD").send_keys("123456@a")
        driver.find_element_by_id("btnLogin").click()

        # 等待左侧菜单栏“车易贷管理”出现之后才点击
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('/html/body/div[4]/div[1]/div/ul/li[3]/ul/li[2]/a')).click()
        
        # 等待“新增”按钮出现才点击
        sleep(1)
        WebDriverWait(driver, 20).until(lambda x: x.find_element_by_id("add")).click()

        # 持续等待并且判断iframe这个元素是否存在，如果存在，返回true 反则返回false.
        bool_display = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_css_selector("#layui-layer1 iframe").is_displayed())

        # 如果返回true,即找到了这个元素，那么说明我可以使用切换iframe的功能了
        if bool_display:
            driver.switch_to_frame("layui-layer-iframe1")

        # 设置表单的值
        sleep(1)
        Select(driver.find_element_by_id("business_type_detail")).select_by_visible_text(u"GPS抵押押证")
        driver.find_element_by_id("model_tb_business_base_info_CUSTOMER_NAME").send_keys(u"紫苏八一五6")
        driver.find_element_by_id("model_tb_business_base_info_PHONE_NUMBER").send_keys("15876366685")
        driver.find_element_by_id("submit").click()

        # 获取成功反馈
        success_text = WebDriverWait(driver, 30).until(lambda x: x.find_element_by_css_selector("#jbox #jbox-content")).text

        # 截取订单号
        businessId = 'TD' + success_text.split("TD")[1]

        self.foo(businessId)

    def foo(self, id): 
        print(id)

    
    # def tearDown(self):
    #     self.driver.quit()
    #     self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


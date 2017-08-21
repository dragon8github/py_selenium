# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from Lib import Lib
import unittest

class AddCarBusiness(unittest.TestCase):
    # 准备环节
    def setUp(self):
        # 启动火狐浏览器并且获得实例对象
        self.driver = webdriver.Firefox()

        # 实例化工具类库Lib
        self.L = Lib(self.driver)

    # 开始
    def test_start(self):
        # 登录
        self.L.login("linxue", "123456@a")

        # 等待左侧菜单栏“车易贷管理”出现之后才点击
        self.L.waitForElementByXpath('/html/body/div[4]/div[1]/div/ul/li[3]/ul/li[2]/a').click()
        
        # 等待js加载完毕
        if self.L.waitForJsLoadFinish():
            # 等待 “新增” 按钮出现 并且 点击“添加”按钮
            self.L.waitForElementByCss('#add').click()

        # 等待iframe并且将当前窗口切换为该iframe
        self.driver.switch_to.frame(self.L.waitForElementByCss('#layui-layer1 iframe'))

        # 设置表单的值
        bool_display = self.L.waitForElementDisplayById('model_tb_business_base_info_BUSINESS_ID')
        if bool_display:
            Select(self.driver.find_element_by_id("business_type_detail")).select_by_visible_text(u"GPS抵押押证")
            self.driver.find_element_by_id("model_tb_business_base_info_CUSTOMER_NAME").send_keys(u"紫苏八一五6")
            self.driver.find_element_by_id("model_tb_business_base_info_PHONE_NUMBER").send_keys("15876366685")
            # 虽然可能性不高，但真的可能框架的JS还没加载好。导致点击无效。
            # 但我又没有必要为了这东西写一个js加载判断。更何况这很难。所以还是用sleep 1秒吧
            self.L.sleep(1, lambda x: x.find_element_by_id("submit").click())

        # 获取成功反馈
        success_text = self.L.waitForElementByCss('#jbox #jbox-content').text

        # 截取订单号
        businessId = 'TD' + success_text.split("TD")[1]

        self.foo(businessId)

    def foo(self, id): 
        print(id)

    # def tearDown(self):
        # self.driver.quit()

if __name__ == "__main__":
    unittest.main()

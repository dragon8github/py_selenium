from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from Lib import Lib
import unittest
import time

customer_name = '紫苏UI1'
shenfenzheng = '220883199002038547'
phone = '15876366685'
jine = '100000'  # 借款金额

businessId = 'TDC1012017081203'


class CarBusiness(unittest.TestCase):
    # 准备环节
    def setUp(self):
        # 启动火狐浏览器并且获得实例对象
        self.driver = webdriver.Firefox()

        # 实例化工具类库Lib
        self.L = Lib(self.driver)

    def test_pianquzhuguan(self):#片区主管
         self.L.login('chenyongkun', '123456@a')
         # self.L.waitForElementByCss(".page-sidebar > ul >li:nth-child(3) > .sub-menu > li:nth-child(1)").click()  # 点击业务审核页面
         self.L.waitForElementByCss(".page-sidebar > ul >li:nth-child(3) > .sub-menu > li:nth-child(1)").click()
         if self.L.waitForJsLoadFinish():
             self.L.setValueById("carBusinessId", businessId)
             self.L.waitForElementByCss("button.btn").click()  # 点击搜索
             self.L.waitForElementByCssWhere(lambda x: self.L.getElementsCountByCss('.table > tbody > tr') == 1,'.table-striped tbody tr td:nth-child(12) a').click()  # 注意这里是确认只显示1条数据才执行，'.table-striped tbody tr td:nth-child(11)'是编辑按钮的css
         # self.L.waitForElementByText(u"提交").click()
         frame = self.L.waitForElementByCss('#layui-layer1 iframe')
         if frame:
             self.driver.switch_to_frame('layui-layer-iframe1')

         self.L.setValueById("log_remark", u"同意提交")
         self.L.waitForElementById("btnSubmit").click()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CarBusiness("test_pianquzhuguan"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from Lib import Lib
import unittest
import time

customer_name = '紫苏UI1'
shenfenzheng = '220883199002038547'
phone = '15876366685'
jine = '100000'  # 借款金额

businessId = 'TDC1012017081203'


class CarBusiness(unittest.TestCase):
    # 准备环节
    def setUp(self):
        self.driver = webdriver.Firefox()

        # 实例化工具类库Lib
        self.L = Lib(self.driver)

    def test_pianquzhuguan(self):
         self.L.login('chenyongkun', '123456@a')
         self.L.waitForElementByCss(".page-sidebar > ul >li:nth-child(3) > .sub-menu > li:nth-child(1)").click()
         if self.L.waitForJsLoadFinish():
            self.L.setValueById("carBusinessId", businessId)
            self.L.waitForElementByCss("button.btn").click() 
            self.L.waitForElementByCssWhere(lambda x: self.L.getElementsCountByCss('.table > tbody > tr') == 1,'.table-striped tbody tr td:nth-child(11) a').click() 


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CarBusiness("test_pianquzhuguan"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

from selenium import webdriver
from selenium.webdriver.support.ui import Select
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
        self.L.login("chaijibing", "123456@a")

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
            self.driver.find_element_by_id("model_tb_business_base_info_CUSTOMER_NAME").send_keys(u"李钊鸿自动化UI测试")
            self.driver.find_element_by_id("model_tb_business_base_info_PHONE_NUMBER").send_keys("13713332652")
            # 虽然可能性不高，但真的可能框架的JS还没加载好。导致点击无效。
            # 但我又没有必要为了这东西写一个js加载判断。更何况这很难。所以还是用sleep 1秒吧
            self.L.sleep(1, lambda x: x.find_element_by_id("submit").click())

        # 获取成功反馈
        success_text = self.L.waitForElementByCss('#jbox #jbox-content').text

        # 截取订单号
        businessId = 'TD' + success_text.split("TD")[1]
        
        # 执行下一步任务
        self.foo(businessId)

    def foo(self, id):
        # 切换回主层面
        self.driver.switch_to.default_content()
        # 关闭目前所在的所有layer. 其实可以直接执行指定的编辑页面js代码：EditBusiness('车易贷'," + id + ")
        self.driver.execute_script("window.layer.closeAll();")
        # 在搜索栏输入id
        self.driver.find_element_by_id("carBusinessId").send_keys(id)
        # 点击搜索
        self.driver.find_element_by_css_selector('#search .btn').click()
        # 等待搜索按钮出现，然后点击它
        self.L.waitForElementByCss('.table > tbody > tr td:nth-child(10) > a').click()    
        # 等待iframe并且将当前窗口切换为该iframe
        self.driver.switch_to.frame(self.L.waitForElementByCss('#layui-layer1 iframe'))
        # 等待一个编辑按钮出来 
        self.L.waitForElementByCss("table#tableCustomer > tbody > tr:nth-child(1) > td:nth-child(7) > a[title='编辑']").click()

    # def tearDown(self):
        # self.driver.quit()

if __name__ == "__main__":
    unittest.main()

from selenium import webdriver
from selenium.webdriver.support.ui import Select
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
           if self.L.waitForElementDisplayById('model_tb_business_base_info_BUSINESS_ID'):
              self.L.waitForSelectTextById('business_type_detail', 'GPS抵押押证')
              self.L.setValueById("model_tb_business_base_info_CUSTOMER_NAME", "李钊鸿自动化UI测试")
              self.L.setValueById("model_tb_business_base_info_PHONE_NUMBER", "13713332652")
              self.L.sleep(0.3, lambda x: x.find_element_by_id("submit").click())

           # 获取成功反馈
           success_text = self.L.waitForElementByCss('#jbox #jbox-content').text

           # 截取订单号
           businessId = 'TD' + success_text.split("TD")[1]

           # 执行下一步任务: 编辑车易贷订单信息
           self.EditCarBusiness(businessId)

    def EditCarBusiness(self, id):
        # 切换回主层面
        self.driver.switch_to.default_content()
        # 关闭目前所在的所有layer. 其实可以直接执行打开编辑页面js代码：EditBusiness('车易贷'," + id + ")
        self.driver.execute_script("window.layer.closeAll();")
        # 在搜索栏输入id
        self.L.setValueById("carBusinessId", id)
        # 点击搜索
        self.driver.find_element_by_css_selector('#search .btn').click()
        # 等待【编辑】按钮出现，然后点击它
        self.L.waitForElementByCss('.table > tbody > tr td:nth-child(10) > a').click()
        # 等待iframe并且将当前窗口切换为该iframe
        self.driver.switch_to.frame(self.L.waitForElementByCss('#layui-layer1 iframe'))
        # 等待一个【编辑】按钮出来
        edit_btn = self.L.waitForElementByCss("table#tableCustomer > tbody > tr:nth-child(1) > td:nth-child(7) > a[title='编辑']")
        # 这里需要等待一下。这是根据观察发现的
        self.L.sleep(1, lambda x: edit_btn.click())

        # 设置表单
        if self.L.waitForElementDisplayById('model_tb_car_personal_id_card_no'):
           self.L.setValueById("model_tb_car_personal_id_card_no", "445222199307100337")
           self.L.setValueById("model_tb_car_personal_nativeplace", "汉")
           self.L.setValueById("model_tb_car_personal_current_address", "详细地址")
           self.L.setValueById("model_tb_car_job_company_name", "单位全称")
           self.L.setValueById("model_tb_car_job_company_address", "单位地址")
           self.L.setValueById("model_tb_car_job_company_phone", "13214785214")
           self.L.setValueById("model_tb_car_job_job_duty", "职位")
           self.L.setValueById("model_tb_car_job_job_pay", "123654")
           self.L.setValueById("model_tb_car_job_other_pay", "369852")
           self.L.setValueById("multiple_customer_bank_info_bank_account", "62534442511225448")
           self.L.setValueById("multiple_customer_bank_info_phone_number", "15876366685")
           self.L.setValueById("multiple_customer_bank_info_bank_subname", "工商支行")

           self.L.waitForSelectTextById('model_tb_car_personal_current_sheng', '广东省')
           self.L.waitForSelectTextById('model_tb_car_personal_current_shi', '广州市')
           self.L.waitForSelectTextById('model_tb_car_personal_current_xian', '东山区')
           self.L.waitForSelectTextById('multiple_customer_bank_info_bank_name', '中国工商银行')
           self.L.waitForSelectTextById('multiple_customer_bank_info_bank_provice', '广东省')
           self.L.waitForSelectTextById('multiple_customer_bank_info_bank_city', '中山市')
           self.L.waitForSelectTextById('multiple_customer_bank_info_output_type', '对私')

        # 保存表单
        self.driver.find_element_by_id('saveRow').click()
        # 点击确定保存
        self.L.waitForElementByCss(".layui-layer-btn0").click()
        # 等待alert并且点击确认
        self.L.waitForAlert().accept()

    # def tearDown(self):
        # self.driver.quit()

if __name__ == "__main__":
    unittest.main()

from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
class Lib:
    # 构造函数
    def __init__(self, driver):
        # webdriver for firefox的实例对象
        self.driver = driver
        # 测试地址
        self.base_url = "http://oatest.bujidele.com:48081/"

    # 登录
    def login(self, username, password):
        self.driver.get(self.base_url + "/Admin/Account/Login")
        self.driver.find_element_by_id("USER_ID").send_keys(username)
        self.driver.find_element_by_id("PASSWORD").send_keys(password)
        self.driver.find_element_by_id("btnLogin").click()

    # 睡眠指定的时间之后，执行回调函数，传入driver， 并且返回结果
    def sleep(self, time, method):
        sleep(time)
        return method(self.driver)

    # 先执行指定的事情，然后再
    def afterSleep(self, time, method):
        value = method(self)
        sleep(time)
        return value

    # 等待Javascript加载完成，也算是等待页面加载完毕
    # 判断方式：.page-sidebar .has-sub.active存在说明js已经加载完毕，并且完成渲染才会存在。
    # 这是自己分析的。如果以后后台代码发生了变化，规则不再如此。可以想办法替换别的规则来判断是否加载完毕
    def waitForJsLoadFinish(self):
        return WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_css_selector(".page-sidebar .has-sub.active").is_displayed())

    def waitForElementByCss(self, path, time = 30):        
        return WebDriverWait(self.driver, time).until(lambda x: x.find_element_by_css_selector(path))

    def waitForElementById(self, path, time = 30):        
        return WebDriverWait(self.driver, time).until(lambda x: x.find_element_by_id(path))

    def waitForElementByXpath(self, path, time = 30):        
        return WebDriverWait(self.driver, time).until(lambda x: x.find_element_by_xpath(path))

    def waitForElementDisplayByCss(self, path, time = 30):
        return WebDriverWait(self.driver, time).until(lambda x: x.find_element_by_css_selector(path).is_displayed())

    def waitForElementDisplayById(self, path, time = 30):
        return WebDriverWait(self.driver, time).until(lambda x: x.find_element_by_id(path).is_displayed())

    def waitForElementDisplayByXpath(self, path, time = 30):
        return WebDriverWait(self.driver, time).until(lambda x: x.find_element_by_xpath(path).is_displayed())



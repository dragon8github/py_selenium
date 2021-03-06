from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep
import re, uuid

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
        self.setValueById("USER_ID", username)
        self.setValueById("PASSWORD", password)
        self.driver.find_element_by_id("btnLogin").click()

    # 睡眠指定的时间之后，执行回调函数，传入driver， 并且返回结果
    def sleep(self, time, method):
        sleep(time)
        return method(self.driver)

    # 先执行指定的事情，然后再睡眠制定的时间
    def afterSleep(self, method, time):
        value = method(self.driver)
        sleep(time)
        return value

    # 等待Javascript加载完成，也算是等待页面加载完毕
    # 判断方式：.page-sidebar .has-sub.active存在说明js已经加载完毕，并且完成渲染才会存在。
    # 这是自己分析的。如果以后后台代码发生了变化，规则不再如此。可以想办法替换别的规则来判断是否加载完毕
    def waitForJsLoadFinish(self):
        return WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_css_selector(".page-sidebar .has-sub.active").is_displayed())

    # 等待指定的元素可选为止。但该元素可以为隐藏，这个搜索方式类似$(element).size() > 1
    # 并且返回该元素，可以继续对元素进行一系列操作，如click()、 send_keys('')
    # 如果条件是需要元素完全可视化，那应该使用下面一套方法
    def waitForElementByCss(self, path, time = 30):        
        return WebDriverWait(self.driver, time).until(lambda x: x.find_element_by_css_selector(path))
    def waitForElementById(self, path, time = 30):        
        return WebDriverWait(self.driver, time).until(lambda x: x.find_element_by_id(path))
    def waitForElementByXpath(self, path, time = 30):        
        return WebDriverWait(self.driver, time).until(lambda x: x.find_element_by_xpath(path))

    # 和上一套类似，都是判断元素是否存在，并且可见。
    # 返回布尔值。注意并不是返回元素本身。所以不能再进行相关操作
    # 某些场景需要元素用户可视再进行操作可以使用这一套
    def waitForElementDisplayByCss(self, path, time = 30):
        return WebDriverWait(self.driver, time).until(lambda x: x.find_element_by_css_selector(path).is_displayed())
    def waitForElementDisplayById(self, path, time = 30):
        return WebDriverWait(self.driver, time).until(lambda x: x.find_element_by_id(path).is_displayed())
    def waitForElementDisplayByXpath(self, path, time = 30):
        return WebDriverWait(self.driver, time).until(lambda x: x.find_element_by_xpath(path).is_displayed())

    # Select元素专用的方法。
    # 可以根据text或者value来选择
    # 它首先会查找并且等待select元素本身，
    # 再等待直到select的html代码中,既option中存在value为止。再进行操作。
    # 这是为了兼容两种情况：1、select元素是异步加载的，2、option的内容是异步加载的
    def waitForSelectTextByCss(self, path, value, time = 30):
        return Select(WebDriverWait(self.driver, time).until(lambda x: value in x.find_element_by_css_selector(path).get_attribute('innerHTML') and x.find_element_by_css_selector(path))).select_by_visible_text(value)
    def waitForSelectTextById(self, path, value, time = 30):
        return Select(WebDriverWait(self.driver, time).until(lambda x: value in x.find_element_by_id(path).get_attribute('innerHTML') and x.find_element_by_id(path))).select_by_visible_text(value)
    def waitForSelectTextByXpath(self, path, value, time = 30):
        return Select(WebDriverWait(self.driver, time).until(lambda x: value in x.find_element_by_xpath(path).get_attribute('innerHTML') and x.find_element_by_xpath(path))).select_by_visible_text(value)
    def waitForSelectValueByCss(self, path, value, time = 30):
        return Select(WebDriverWait(self.driver, time).until(lambda x: value in x.find_element_by_css_selector(path).get_attribute('innerHTML') and x.find_element_by_css_selector(path))).select_by_value(value)
    def waitForSelectValueById(self, path, value, time = 30):
        return Select(WebDriverWait(self.driver, time).until(lambda x: value in x.find_element_by_id(path).get_attribute('innerHTML') and x.find_element_by_id(path))).select_by_value(value)
    def waitForSelectValueByXpath(self, path, value, time = 30):
        return Select(WebDriverWait(self.driver, time).until(lambda x: value in x.find_element_by_xpath(path).get_attribute('innerHTML') and x.find_element_by_xpath(path))).select_by_value(value)


    # 先清空值，再进行输入
    def setValueById(self, key, value):
        element = self.waitForElementById(key)
        element.clear()
        element.send_keys(value)    
    def setValueByCss(self, key, value):
        element = self.waitForElementByCss(key)
        element.clear()
        element.send_keys(value)    
    def setValueByXpath(self, key, value):
        element = self.waitForElementByXpath(key)
        element.clear()
        element.send_keys(value)

    # 判断alert是否存在，如果存在。返回alert实例，否则返回False
    def alertIsPresent(self):
        try:
            _alert = self.driver.switch_to.alert
            # 通过这一步判断是否会报错。这一步的作用仅仅如此
            _alert.text
            # 如果上一步都没有报错，那么就返回这个实例吧
            return _alert
        except:
            return False

    # 等待alert出现
    def waitForAlert(self, time = 30):
        return WebDriverWait(self.driver, time).until(lambda x: self.alertIsPresent())

    # 当(回调函数)条件满足且元素存在的时候，才返回元素
    def waitForElementByCssWhere(self, method, path, time = 30):
        return WebDriverWait(self.driver, time).until(lambda x: method(x) and x.find_element_by_css_selector(path))

    # 获取元素的数量, 如果元素不存在则返回0
    def getElementsCountByCss(self, path):
        return len(self.driver.find_elements_by_css_selector(path))
    def getElementsCountById(self, path):
        return len(self.driver.find_element_by_id(path))
    def getElementsCountByXpath(self, path):
        return len(self.driver.find_element_by_xpath(path))

    # 如果条件表达式不为True的时候，那么就继续执行某个表达式
    def execWhere(self, condition_method, main_method, time = 30):
        return WebDriverWait(self.driver, time).until(lambda x: condition_method(x) and main_method(x))
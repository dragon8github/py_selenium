from selenium.webdriver.support.wait import WebDriverWait

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

    # js已经加载完毕
    # 判断方式：.page-sidebar .has-sub.active存在说明js已经加载完毕，并且完成渲染才会存在。
    # 这是自己分析的。如果以后后台代码发生了变化，规则不再如此。可以想办法替换别的规则来判断是否加载完毕
    def jsLoad(self):
        return WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_css_selector(".page-sidebar .has-sub.active").is_displayed())
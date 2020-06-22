from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
import pytest,json

from page.App import App


class TestXueQiu:
    @classmethod
    def setup_class(cls):
        #静默运行，先创建一个Options对象，调用add_argument参数
        #options=Options()
        #options.add_argument('--headless')
        # driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME) #传入options对象
        # driver.implicitly_wait(30)
        cls.mainPage=App.main()
    def setup_method(self):
        self.loginPage=self.mainPage.go_to_LoginPage()

    def test_demo01(self):
        # driver=setup
        # driver.get("https://www.baidu.com")
        # js=driver.execute_script("return JSON.stringify(window.performance.timing)")
        # print(json.dumps(json.loads(js),indent=4))
        # driver.find_element(By.CSS_SELECTOR,'a[data-analytics-data*="雪球图标"]')
        # driver.refresh()
        pass

    def test_login(self):
        pass




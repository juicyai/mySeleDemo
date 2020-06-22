from selenium.webdriver.common.by import By

from driver.Client import Client


class BasePage:

    def __init__(self):
        self._driver=self.getDriver()
        #self._driver.get("https://xueqiu.com/")
        #self.driver
    @classmethod
    def getClient(cls):
        return Client

    @classmethod
    def getDriver(cls):
        driver=cls.getClient().driver
        return driver

    def find(self,by,value):
        return self._driver.find_element(by,value)




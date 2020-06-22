"""定义客户端"""
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver


class Client:
    driver:WebDriver
    @classmethod
    def initial_web(cls):
        cls.driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        cls.driver.get("https://xueqiu.com/")
        cls.driver.implicitly_wait(30)
        return cls.driver


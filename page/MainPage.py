
from page.BasePage import BasePage
from page.LoginPage import LoginPage
from selenium.webdriver.common.by import By
class MainPage(BasePage):

    def go_to_LoginPage(self):
        self.find(By.XPATH,"//span[text()='登录/注册']").click()
        return LoginPage()


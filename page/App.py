from page.BasePage import BasePage


class App(BasePage):
    @classmethod
    def main(cls):
        cls.getClient().initial_web()
        from page.MainPage import MainPage
        return MainPage()

App.main()
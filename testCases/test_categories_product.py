import time

from Utilies.readProperties import ReadConfig
from Utilies.CustomLogger import LogGen
from PageObjects.LogIn_page import LogInPage
from PageObjects.Categories_product import Categories


class TestCategories:
    url = ReadConfig.get_application_url()
    user_name = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    loggen = LogGen.loggen()

    def test_categories(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.login = LogInPage(self.driver)
        self.login.set_username(self.user_name)
        self.login.set_password(self.password)
        self.login.click_login()

        self.cate = Categories(self.driver)
        self.cate.click_catalog()
        self.cate.click_categories()
        self.cate.enter_value("computers")
        self.cate.click_publish()
        self.cate.click_search()
        time.sleep(5)




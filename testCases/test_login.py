import pytest

from PageObjects.LogIn_page import LogInPage
from Utilies.readProperties import ReadConfig
from Utilies.CustomLogger import LogGen


class Test_002_LogIn:
    url = ReadConfig.get_application_url()
    user_name = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    # @pytest.mark.regression
    # @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("******Login Page Title Checking Start*******")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        self.loginPage = LogInPage(self.driver)
        self.loginPage.set_username(self.user_name)
        self.loginPage.set_password(self.password)
        self.loginPage.click_login()

        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("***** Login Page Title Is Matched*****")
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + " test_login.png")
            self.logger.info("***** Login Page Title Is Not Matched*****")

            self.driver.close()
            assert False

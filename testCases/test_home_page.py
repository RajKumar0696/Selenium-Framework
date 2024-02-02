import pytest

from PageObjects.Home_page import HomePage
from Utilies.readProperties import ReadConfig
from Utilies.CustomLogger import LogGen


class Test_001_HomePage:
    url = ReadConfig.get_application_url()
    user_name = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    # @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*****Test_001_LogIn*******")
        self.logger.info("* ***** Home Page Title Checking *******")
        self.driver = setup
        self.driver.get(self.url)
        self.homPage = HomePage(self.driver)
        act_title = self.homPage.get_title()
        if act_title == "Your store. Login":
            self.logger.info("***** Home Page Title Is Matched *****")
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\ " + "test_homePageTitle.png")
            self.logger.info("******Home Page Title Is Not Matched*******")
            self.driver.close()
            assert False

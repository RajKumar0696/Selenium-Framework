import time
import pytest
from PageObjects.LogIn_page import LogInPage
from Utilies.readProperties import ReadConfig
from Utilies.CustomLogger import LogGen
from PageObjects.add_customer_page import AddNewCustomer
from PageObjects.search_customer_page import SearchCustomer


class Test_004_SearchCustomer:
    url = ReadConfig.get_application_url()
    user_name = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_customer(self, setup):
        self.logger.info("*** Test_004_search_customer***")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.lp = LogInPage(self.driver)
        self.lp.set_username(self.user_name)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("*** Login successfully***")

        self.logger.info("*** Starting Search customers by email ***")
        self.addCustomer = AddNewCustomer(self.driver)
        self.addCustomer.click_on_customer_menu()
        self.addCustomer.click_on_customers_menu_item()

        self.logger.info("*** Search customers by email ***")
        search_cust = SearchCustomer(self.driver)
        search_cust.search_by_email("kiyjcycyhjc676008@gmail.com")
        search_cust.click_search()
        time.sleep(5)
        status = search_cust.search_customer_email("kiyjcycyhjc676008@gmail.com")
        assert True == status
        self.logger.info("*** Search customer_004 test is completed ***")

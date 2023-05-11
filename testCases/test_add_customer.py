import random
import string

import pytest
from selenium.webdriver.common.by import By

from PageObjects.LogIn_page import LogInPage
from Utilies.readProperties import ReadConfig
from Utilies.CustomLogger import LogGen
from PageObjects.add_customer_page import AddNewCustomer


class Test_003_AddCustomer:
    url = ReadConfig.get_application_url()
    user_name = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_customer(self, setup):
        self.logger.info("*** Test_003_add_customer***")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.lp = LogInPage(self.driver)
        self.lp.set_username(self.user_name)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("*** Login successfully***")

        self.logger.info("*** Starting add customer test***")
        self.addCustomer = AddNewCustomer(self.driver)
        self.addCustomer.click_on_customer_menu()
        self.addCustomer.click_on_customers_menu_item()
        self.addCustomer.click_on_add_new_button()
        self.logger.info("*** Providing customer details ***")

        # Here we are creating random email generation
        self.email = random_generator() + "@gmail.com"
        self.addCustomer.set_email(self.email)
        self.addCustomer.set_password("test-003")
        self.addCustomer.set_first_name("Raj")
        self.addCustomer.set_last_name("Kumar")
        self.addCustomer.set_gender("Male")
        self.addCustomer.set_date("06/25/1996")
        self.addCustomer.set_company_name("Sree")
        self.addCustomer.set_customer_role("Registered")
        self.addCustomer.admin_comment_box("Hi this is RajKumar")
        self.addCustomer.click_on_save()

        self.logger.info("*** Customer added successfully ***")
        self.logger.info("*** Add customer validation start ***")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*** Add customer test passed ***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_customer_scr.png")
            assert True == False

        self.driver.close()
        self.logger.info("*** Ending Add customer test ***")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))

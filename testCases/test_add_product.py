import pytest
from selenium.webdriver.common.by import By

from PageObjects.LogIn_page import LogInPage
from Utilies.readProperties import ReadConfig
from Utilies.CustomLogger import LogGen
from PageObjects.add_product import AddProducts


class Test_006_AddCustomer:
    url = ReadConfig.get_application_url()
    user_name = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_product(self, setup):
        self.logger.info("*** Test_006_add_product***")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.lp = LogInPage(self.driver)
        self.lp.set_username(self.user_name)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("*** Login successfully***")

        self.logger.info("***Starting add product test***")
        self.add_product = AddProducts(self.driver)
        self.add_product.click_catalog()
        self.add_product.click_products()
        self.add_product.click_add_new()
        self.add_product.click_product_info()

        self.logger.info("***Product details provided here***")
        self.add_product.set_product_name("Monitor")
        self.add_product.set_description("This monitor is very good-looking and good-product")
        self.add_product.click_and_select_categories("Computer")
        self.add_product.click_and_select_categories("Computers >> Desktops")
        self.add_product.click_and_select_manufactures("Apple")
        self.add_product.click_and_select_manufactures("HP")
        self.add_product.set_product_tags("computer")
        self.add_product.click_save()
        self.logger.info("***Product added successfully***")
        self.logger.info("***Added product validation start***")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "The new product has been added successfully." in self.msg:
            assert True == True
            self.logger.info("***Add product test passed***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_add_product_sct.png")
            assert True == False
            self.logger.info("***Add product test case failed***")
        self.driver.close()

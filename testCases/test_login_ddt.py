import pytest

from PageObjects.LogIn_page import LogInPage
from Utilies.readProperties import ReadConfig
from Utilies.CustomLogger import LogGen
from Utilies import ExcelUtils
import time


class Test_002_LogIn_DDT:
    url = ReadConfig.get_application_url()
    path = ".//Test_data/login_test_data.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("****** Test_002_DDT_Login******")
        self.logger.info("****** Verifying Login DDT Test *******")
        self.driver = setup
        self.driver.get(self.url)
        self.loginPage = LogInPage(self.driver)
        self.lp = LogInPage(self.driver)
        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet4')
        print("Number Of Rows in a Excel:", self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.path, 'Sheet4', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet4', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet4', r, 3)

            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Passed ****")
                    self.lp.click_logout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("**** Failed ****")
                    self.lp.click_logout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*** Passed ***")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("*** Login DDT Test Passed ***")
            self.driver.close()
            assert True

        else:
            self.logger.info("*** Login DDT Test Filed***")
            self.driver.close()
            assert False

        self.logger.info("*** End of Login DDt Test***")
        self.logger.info("*** Completed TC_LoginDDT_002 ***")

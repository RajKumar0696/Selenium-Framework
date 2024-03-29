import pytest
from selenium.webdriver.common.by import By
import unittest


class LogInPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//div[@class='buttons']//button"
    button_logout_xpath = "//li[@class='nav-item']//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    # @unittest.skip("Just for trail")
    def set_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

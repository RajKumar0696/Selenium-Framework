import time

from selenium.webdriver.common.by import By

import XL_utils
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
ser_obj = Service(r"C:\Users\WELCOME\Downloads\chromedriver-win64\chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

path = r"D:\python_files\nopcommerce_Project\Test_data\login_test_data.xlsx"

email_id = "Email"
password_id = "Password"
btn_login_xpath = "//div[@class='buttons']//button"
btn_logout_xpath = "//li[@class='nav-item']//a[normalize-space()='Logout']"
driver.get("https://admin-demo.nopcommerce.com/login")

row_max = XL_utils.get_row_count(path, "Sheet4")

for r in range(2, row_max+1):
    email_value = XL_utils.read_data(path, "Sheet4", r, 1)
    password_value = XL_utils.read_data(path, "Sheet4", r, 2)

    driver.find_element(By.ID, email_id).clear()
    driver.find_element(By.ID, email_id).send_keys(email_value)
    driver.find_element(By.ID, password_id).clear()
    driver.find_element(By.ID, password_id).send_keys(password_value)
    driver.find_element(By.XPATH, btn_login_xpath).click()
    time.sleep(5)
    title_page = driver.title
    if title_page == "Dashboard / nopCommerce administration":
        driver.find_element(By.XPATH, btn_logout_xpath).click()
        XL_utils.write_data(path, "Sheet4", r, 4, "Pass")
        XL_utils.fill_green_color(path, "Sheet4", r, 4)
    else:
        XL_utils.write_data(path, "Sheet4", r, 4, "Fail")
        XL_utils.fill_red_color(path, "Sheet4", r, 4)
driver.close()

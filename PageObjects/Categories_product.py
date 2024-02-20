from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest

class Categories:
    catalog_xpath = "//a[@href='#']//p[contains(text(),'Catalog')]"
    categories_xpath = "//p[normalize-space()='Categories']"
    txt_search_box_id = "SearchCategoryName"
    drop_published_id = "SearchPublishedId"
    btn_search_id = "search-categories"

    # After searching product edit the name,description etc.
    edit_button_xpath = "//a[normalize-space()='Edit']"
    text_name_id = "Name"
    text_desc_xpath = "//div[@class='tox-sidebar-wrap']"
    drop_parent_id = "ParentCategoryId"
    text_display_order_xpath = "//input[@title='2 ']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_catalog(self):
        self.driver.find_element(By.XPATH, self.catalog_xpath).click()

    def click_categories(self):
        self.driver.find_element(By.XPATH, self.categories_xpath).click()

    def enter_value(self, value):
        self.driver.find_element(By.ID, self.txt_search_box_id).send_keys(value)

    def click_publish(self):
        drp = Select(self.driver.find_element(By.ID, self.drop_published_id))
        drp.select_by_index(1)
        drp.select_by_index(2)
        drp.select_by_index(0)

    def click_search(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def click_edit_button(self):
        self.driver.find_element(By.XPATH, self.edit_button_xpath).click()

    def change_product_name(self, name):
        self.driver.find_element(By.ID, self.text_name_id).clear()
        self.driver.find_element(By.ID, self.text_name_id).send_keys(name)

    def add_description_value(self, desc):
        self.driver.find_element(By.ID, self.text_desc_xpath).clear()
        self.driver.find_element(By.ID, self.text_desc_xpath).send_keys(desc)

    def click_parent_
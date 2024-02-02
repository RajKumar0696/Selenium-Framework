import time

from selenium.webdriver.common.by import By


class AddProducts:
    lik_cust_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/a"
    lik_product_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[1]/a"
    btn_add_new_xpath = "//a[normalize-space()='Add new']"
    lik_product_info_xpath = "//div[@class='card-title'][normalize-space()='Product info']"
    txt_product_name_xpath = "//*[@id='Name']"
    txt_product_disc_xpath = "//textarea[@id='ShortDescription']"
    txt_categories_xpath = "//textarea[@id='ShortDescription']"
    lik_computers_xpath = "(//div[@role='listbox'])[1]"
    lik_computers_desktop_xpath = "(//li[normalize-space()='Computers >> Desktops'])[1]"
    lik_computers_notebook_xpath = "//li[normalize-space()='Computers >> Notebooks']"
    lik_computers_software_xpath = "(//li[normalize-space()='Computers >> Software'])[1]"
    lik_electronics_xpath = "(//li[normalize-space()='Electronics'])[1]"
    lik_apparel_xpath = "(//li[normalize-space()='Apparel'])[1]"
    lik_gift_card_xpath = "(//li[@id='766c6fca-88b3-40ed-b84d-7062ff3fb0f8'])[1]"
    txt_manufactures_xpath = "(//div[@role='listbox'])[2]"
    lik_apple_xpath = "(//li[normalize-space()='Apple'])[1]"
    lik_hp_xpath = "(//li[normalize-space()='HP'])[1]"
    lik_nike_xpath = "(//li[normalize-space()='Nike'])[1]"
    txt_product_tag_xpath = "(//ul[@class='tag-editor ui-sortable'])[1]"
    btn_save_xpath = "//button[@name='save']"

    # The new product has been added successfully.

    def __init__(self, driver):
        self.driver = driver

    def click_catalog(self):
        self.driver.find_element(By.XPATH, self.lik_cust_menu_xpath).click()

    def click_products(self):
        self.driver.find_element(By.XPATH, self.lik_product_xpath).click()

    def click_add_new(self):
        self.driver.find_element(By.XPATH, self.btn_add_new_xpath).click()

    def click_product_info(self):
        self.driver.find_element(By.XPATH, self.lik_product_info_xpath).click()

    def set_product_name(self, product_name):
        self.driver.find_element(By.XPATH, self.txt_product_name_xpath).send_key(product_name)

    def set_description(self, disc):
        self.driver.find_element(By.XPATH, self.txt_product_disc_xpath).send_key(disc)

    def click_and_select_categories(self, category):
        self.driver.find_element(By.XPATH, self.txt_categories_xpath).click()
        time.sleep(5)
        if category == "Computers":
            self.driver.find_element(By.XPATH, self.lik_computers_xpath).click()
        elif category == "Computers >> Desktops":
            self.driver.find_element(By.XPATH, self.lik_computers_desktop_xpath).click()
        elif category == "Computers >> Notebooks":
            self.driver.find_element(By.XPATH, self.lik_computers_notebook_xpath).click()
        elif category == "Computers >> Software":
            self.driver.find_element(By.XPATH, self.lik_computers_software_xpath).click()
        elif category == "Electronics":
            self.driver.find_element(By.XPATH, self.lik_electronics_xpath).click()
        elif category == "Apparel":
            self.driver.find_element(By.XPATH, self.lik_apparel_xpath).click()
        elif category == "Gift Cards":
            self.driver.find_element(By.XPATH, self.lik_gift_card_xpath).click()
        else:
            print("Your given category is not in the list")

    def click_and_select_manufactures(self, manufacture_name):
        self.driver.find_element(By.XPATH, self.txt_manufactures_xpath).click()

        if manufacture_name == "Apple":
            self.driver.find_element(By.XPATH, self.lik_apple_xpath).click()
        elif manufacture_name == "HP":
            self.driver.find_element(By.XPATH, self.lik_hp_xpath).click()
        elif manufacture_name == "Nike":
            self.driver.find_element(By.XPATH, self.lik_nike_xpath).click()
        else:
            print("Your given manufacture name not in the list")

    def set_product_tags(self, tag_name):
        self.driver.find_element(By.XPATH, self.txt_product_tag_xpath).send_keys(tag_name)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

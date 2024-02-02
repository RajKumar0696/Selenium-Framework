from selenium.webdriver.common.by import By
import time


class AddNewCustomer:
    # Elements
    lnk_customers_menu_xpath = "(//a[@class='nav-link'])[21]"
    lnk_customers_menu_item_xpath = "(//p[contains(text(),'Customers')])[2]"
    btn_add_new_xpath = "(//a[normalize-space()='Add new'])[1]"
    txt_email_id = "Email"
    txt_password_id = "Password"
    txt_first_name_id = "FirstName"
    txt_last_name_id = "LastName"
    rdo_gender_male_id = "Gender_Male"
    rdo_gender_female_id = "Gender_Female"
    txt_date_picker_id = "DateOfBirth"
    txt_company_name_id = "Company"
    rdo_tax_exempt_xpath = "//input[@id='IsTaxExempt']"
    txt_news_letter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    link_your_story_name_xpath = "//li[normalize-space()='Your store name']"
    link_test_store2_xpath = "//li[normalize-space()='Test store 2']"
    txt_customer_role_xpath = "(//div[@role='listbox'])[2]"
    link_administrators_xpath = "//li[normalize-space()='Administrators']"
    link_forum_moderators_xpath = "//li[normalize-space()='Forum Moderators']"
    link_guests_xpath = "//li[normalize-space()='Guests']"
    link_registered_xpath = "//li[normalize-space()='Registered']"
    link_vendors_xpath = "//li[contains(text(),'Vendors')]"
    drp_manage_of_vendor_id = "VendorId"
    rdo_active_xpath = "//input[@id='Active']"
    txt_admin_comment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_customer_menu(self):
        self.driver.find_element(By.XPATH, self.lnk_customers_menu_xpath).click()

    def click_on_customers_menu_item(self):
        self.driver.find_element(By.XPATH, self.lnk_customers_menu_item_xpath).click()

    def click_on_add_new_button(self):
        self.driver.find_element(By.XPATH, self.btn_add_new_xpath).click()

    def set_email(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def set_first_name(self, firstname):
        self.driver.find_element(By.ID, self.txt_first_name_id).send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element(By.ID, self.txt_last_name_id).send_keys(lastname)

    def set_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdo_gender_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdo_gender_female_id).click()

    def set_date(self, date):
        self.driver.find_element(By.ID, self.txt_date_picker_id).send_keys(date)

    def set_company_name(self, comname):
        self.driver.find_element(By.ID, self.txt_company_name_id).send_keys(comname)

    def set_customer_role(self, role):
        self.driver.find_element(By.XPATH, self.txt_customer_role_xpath).click()
        time.sleep(5)
        if role == 'Administrators':
            self.driver.find_element(By.XPATH, self.link_administrators_xpath).click()
        elif role == 'Forum Moderators':
            self.driver.find_element(By.XPATH, self.link_forum_moderators_xpath).click()
        elif role == 'Registered':
            self.driver.find_element(By.XPATH, self.link_registered_xpath).click()

    def admin_comment_box(self, comment):
        self.driver.find_element(By.XPATH, self.txt_admin_comment_xpath).send_keys(comment)

    def click_on_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

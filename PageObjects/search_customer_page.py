from selenium.webdriver.common.by import By


class SearchCustomer:
    txt_email_id = "SearchEmail"
    txt_first_name_id = "SearchFirstName"
    txt_last_name_id = "SearchLastName"
    btn_search_id = "search-customers"

    table_xpath = "//div[@id='customers-grid_wrapper']//div[@class='row']"
    table_row_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_column_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def search_by_email(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def search_by_first_name(self, f_name):
        self.driver.find_element(By.ID, self.txt_first_name_id).clear()
        self.driver.find_element(By.ID, self.txt_first_name_id).send_keys(f_name)

    def search_by_last_name(self, l_name):
        self.driver.find_element(By.ID, self.txt_last_name_id).clear()
        self.driver.find_element(By.ID, self.txt_last_name_id).send_keys(l_name)

    def click_search(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def get_number_of_rows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_row_xpath))

    def get_number_of_columns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_column_xpath))

    def search_customer_email(self, email):
        flag = False
        for r in range(1, self.get_number_of_rows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            email_id=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if email_id == email:
                flag = True
                break
        return flag

    def search_customer_name(self,name):
        flag = False
        for r in range(1,self.get_number_of_rows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if name==name:
                flag = True
                break
        return flag


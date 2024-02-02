from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# path = "D:\python_files\nopcommerce_Project\path1/chromedriver.exe"
path = r"path1/chromedriver.exe"
ser_obj = Service(path)

driver = webdriver.Chrome(executable_path=path)
driver.get("https://www.youtube.com/shorts/9vTzKNXvozE")

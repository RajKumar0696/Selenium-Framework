# which are all we use common in all class/methods/function that codes will create here
# and should use @pytest.fixture()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        path = r"C:\Users\WELCOME\Downloads\chromedriver_win32\chromedriver.exe"
        ser_obj = Service(path)
        driver = webdriver.Chrome(service=ser_obj, options=options)
        print("This is chrome browser")

    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("This is Firefox browser")


    else:
        driver = webdriver.Ie
        print("This is Internet Explorer browser")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI methods
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

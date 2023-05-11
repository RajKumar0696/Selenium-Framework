# which are all we use common in all class/methods/function that codes will create here
# and should use @pytest.fixture()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
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
def browser(request):  # This will return the browser value to set up method
    return request.config.getoption("--browser")


# ***** PYTEST HTML REPORT******

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Modual Name'] = 'Customer'
    config._metadata['Tester'] = 'Rajkumar'


# It is hook for delete/modify Environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

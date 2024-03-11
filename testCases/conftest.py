# which are all we use common in all class/methods/function that codes will create here
# and should use @pytest.fixture()


from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        from selenium.webdriver.chrome.service import Service as ChromeService
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        print("This is chrome browser")

    elif browser == "firefox":
        # from selenium.webdriver.firefox.service import Service as FirefoxService
        # from webdriver_manager.firefox import GeckoDriverManager
        #
        # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver = webdriver.Firefox()
        print("This is Firefox browser")

    elif browser == "edge":
        # from selenium.webdriver.edge.service import Service as EdgeService
        # from webdriver_manager.microsoft import EdgeChromiumDriverManager
        #
        # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver = webdriver.Edge()
        print("This is Edge browser")

    else:
        from selenium.webdriver.ie.service import Service as IEService
        from webdriver_manager.microsoft import IEDriverManager

        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
        # driver = webdriver.Ie()
        # print("This is Internet Explorer browser")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI methods
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to set up method
    return request.config.getoption("--browser")
#
#
# # ***** PYTEST HTML REPORT******
#
# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop commerce'
#     config._metadata['Modual Name'] = 'Customer'
#     config._metadata['Tester'] = 'Rajkumar'
#
#
# # It is hook for delete/modify Environment info to HTML Report
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

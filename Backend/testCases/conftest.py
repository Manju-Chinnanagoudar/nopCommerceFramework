from selenium import webdriver
import pytest
from utilities.logger_utility import custom_logger


@pytest.fixture()
def setup(request):
    #logger = custom_logger().getlog()
    browser = request.config.getoption("--browser")
    try:
        if browser == 'chrome':
            driver = webdriver.Chrome(
                executable_path='E:\projects\selenium\chromedriver_win32\chromedriver.exe')
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'ie':
            driver = webdriver.Ie()
        elif browser == 'edge':
            driver = webdriver.Edge(
                executable_path='Backend\Webdrivers\msedgedriver.exe')
        elif browser == 'safari':
            driver = webdriver.safari()
        else:
            chrome_options = webdriver.chrome.options.Options()
            chrome_options.headless = True
            driver = webdriver.Chrome(options=chrome_options,
                                      executable_path='E:\projects\selenium\chromedriver_win32\chromedriver.exe')
        #logger.info('*------Chrome Browser Initiated')
        driver.maximize_window()
        yield driver
        driver.close()
    except:
        pass
        #logger.critical('!!!!... Browser Setup failed')


def pytest_addoption(parser):
    """
    Method to pass the brwoser value through Cmd
    """
    parser.addoption("--browser", help="Select the browser")

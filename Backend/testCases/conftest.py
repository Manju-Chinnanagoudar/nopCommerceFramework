from selenium import webdriver
import pytest
from utilities.logger_utility import custom_logger


@pytest.fixture()
def setup():
    #logger = custom_logger().getlog()
    try:
        driver = webdriver.Chrome(
            executable_path='E:\projects\selenium\chromedriver_win32\chromedriver.exe')
        driver.maximize_window()
        #logger.info('*------Chrome Browser Initiated')
        yield driver
        driver.close()
    except:
        pass
        #logger.critical('!!!!... Browser Setup failed')

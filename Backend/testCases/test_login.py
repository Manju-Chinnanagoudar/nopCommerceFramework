import pytest
from selenium import webdriver
import unittest

from pageObjects.loginPage import LoginPage
from utilities.read_property import ReadConfig
from utilities.logger_utility import custom_logger

logger = custom_logger().getlog()


@pytest.mark.usefixtures("setup")
class Test_001_Login(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.driver.get(ReadConfig.get_URL())
        self.lp = LoginPage(self.driver)

    def test_login_page_title(self):
        logger.info('*** Login Page Title validation started')
        if self.lp.validate_page_title('Your store. Login'):
            logger.info("Page title is 'Your store. Login'")
            logger.info("Login Page title validation completed")
        else:
            self.lp.screenshot('PageTitleNotMatch')
            logger.warning(
                '!!! Login Page validation failure, Screenshot captured')
            assert False
        # self.driver.close()

    def test_login(self):
        #self.driver = setup
        # self.driver.get(self._base_URL)
        #self.lp = LoginPage(self.driver)
        logger.info('*** Login Test started')
        self.lp.log_in(ReadConfig.get_EmailID(), ReadConfig.get_Password())
        if self.lp.validate_page_title('Dashboard / nopCommerce administration'):
            logger.info('*** Login Test completed')
        else:
            logger.warning('!!! Login Test Failed')
            self.lp.screenshot('LoginFail')
            assert False
        # self.driver.close()

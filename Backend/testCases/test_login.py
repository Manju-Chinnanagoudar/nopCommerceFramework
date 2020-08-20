import pytest
from selenium import webdriver
import unittest

from pageObjects.loginPage import LoginPage
from utilities.read_property import ReadConfig
from utilities.logger_utility import custom_logger


@pytest.mark.usefixtures("setup")
class Test_001_Login(unittest.TestCase):

    logger = custom_logger.cust_log()

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.logger.info('---------Testing started')
        self.driver = setup
        self.driver.get(ReadConfig.get_URL())
        self.lp = LoginPage(self.driver)

    def test_login_page_title(self):
        if self.lp.validate_page_title('Your store. Login'):
            print("Page title is 'Your store. Login'")
        else:
            self.lp.screenshot('PageTitleNotMatch')
            assert False
        # self.driver.close()

    def test_login(self):
        #self.driver = setup
        # self.driver.get(self._base_URL)
        #self.lp = LoginPage(self.driver)
        self.lp.log_in(ReadConfig.get_EmailID(), ReadConfig.get_Password())
        if self.lp.validate_page_title('Dashboard / nopCommerce administration'):
            print('Logged in Successfully')
        else:
            print('Login Failed')
            self.lp.screenshot('LoginFail')
            assert False
        # self.driver.close()

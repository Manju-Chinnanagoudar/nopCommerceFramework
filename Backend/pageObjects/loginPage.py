from base.basePage import BasePage
from selenium.common.exceptions import WebDriverException

from traceback import print_stack


class LoginPage(BasePage):

    # locators
    _email_textbox = 'Email'
    _password_textbox = 'Password'
    _rememberMe_checkbox = 'RememberMe'
    _login_button = '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input'
    _logout_button = '/html/body/div[3]/div[1]/div/div/ul/li[3]/a'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def log_in(self, email, password, rememberMe='No'):
        """
        Log in function:
        parmas: email: Email of the user
                password: Password of the user
                rememberMe: Yes/No (Default is No)
                        If Yes, clicks on Remember Me check box
        """
        try:
            _email_element = self.driver.find_element_by_id(
                self._email_textbox)
            _password_element = self.driver.find_element_by_id(
                self._password_textbox)
            _rememberMe_element = self.driver.find_element_by_id(
                self._rememberMe_checkbox)
            _login_element = self.driver.find_element_by_xpath(
                self._login_button)

            self.send_keys_to(_email_element, email)
            self.send_keys_to(_password_element, password)
            if rememberMe == 'Yes':
                self.click_element(_rememberMe_element)
            self.click_element(_login_element)
        except:
            print_stack()

import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from traceback import print_stack
from utilities.logger_utility import custom_logger


class Actions:

    def __init__(self, driver):
        self.driver = driver
        self.logger = custom_logger().getlog()
        self.actions = ActionChains(driver)

    def get_title(self):
        """
        Returns the title of the page
        """
        self.logger.info(
            '*** Title of the page "{}" retrived'.format(self.driver.title))
        return self.driver.title

    def send_keys_to(self, element, data):
        try:
            element.clear()
            element.send_keys(data)
            self.logger, info(
                '*** Entered {0} to the field {1}'.format(data, element))
        except WebDriverException:
            self.logger.error(
                '!!! Failed to send text to {} field'.format(element))

    def click_element(self, element):
        try:
            element.click()
        except WebDriverException:
            print_stack()

    def get_text(self, element):
        try:
            element.text
        except WebDriverException:
            print_stack()

    def scroll(self, action='up'):
        if action == 'up':
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if action == 'down':
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def drop_down(self, element, selector, select_by='visible text'):
        try:
            drp = Select(element)
            if select_by == 'visible text':
                drp.select_by_visible_text(selector)
            elif select_by == 'value':
                drp.select_by_value(a)
            elif select_by == 'index':
                drp.select_by_index(a)
            else:
                print('Invalid selection of the selector')
        except:
            print_stack()

    def alert_handle(self, action='accept'):
        if action == 'accept':
            self.driver.switch_to_alert().accept()
        elif action == 'dsimiss':
            self.driver.switch_to_alert().dismiss()

    def screenshot(self, name):

        file_name = name+'.'+str(round(time.time()*1000))+'.png'
        dir_path = 'Backend/Screenshots/'
        rel_path = dir_path + file_name

        try:
            self.driver.save_screenshot(rel_path)
            print('Screenshot saved in the path: '+rel_path)
        except:
            print('Screenshot failed')
            print_stack()

    def right_click(self, element):
        self.actions.context_click(element).perform()

    def double_click(self, element):
        self.actions.double_click(element).perform()

    def hover_mouse(self, element):
        try:
            self.actions.move_to_element(element).perform()
        except WebDriverException:
            print_stack()

    def drag_drop(self, sorce_element, target_element):
        self.driver.maximize_window()
        try:
            self.actions.drag_and_drop(sorce_element, target_element).perform()
        except:
            print_stack()

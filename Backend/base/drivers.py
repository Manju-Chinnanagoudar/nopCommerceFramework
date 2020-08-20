from selenium import webdriver


class WebDriverSelection:
    def __init__(self, browser):
        self.browser = browser

    def get_driver(self):
        if self.browser == 'chrome':
            driver = webdriver.Chrome()
        elif self.browser == 'firefox':
            driver = webdriver.Firefox()
        elif self.browser == 'ie':
            driver = webdriver.Ie()
        elif self.browser == 'edge':
            driver = webdriver.Edge()
        elif self.browser == 'safari':
            driver = webdriver.safari()
        else:
            driver = webdriver.Chrome()

        driver.maximize_window()
        return driver

from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(
        executable_path='E:\projects\selenium\chromedriver_win32\chromedriver.exe')
    driver.maximize_window()
    yield driver
    driver.close()

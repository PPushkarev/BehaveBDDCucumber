


import datetime

import pytest
from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope='function')
def driver():
    service = Service("C:\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    yield driver

    driver.quit()


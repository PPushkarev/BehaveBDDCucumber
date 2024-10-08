from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):
        self.driver = driver

    confirm_text = 'Edit your account information'

    def check_account_enter(self):
        return self.driver.find_element(By.LINK_TEXT, self.confirm_text).is_displayed()

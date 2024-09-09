from selenium.webdriver.common.by import By
from features.pages.accountpage import AccountPage
from features.pages.basepage import BasePage


class LoginPage(BasePage):

    Email = (By.ID, "input-email")
    Pasword = (By.ID, "input-password")
    login_button = (By.CSS_SELECTOR, "input[class='btn btn-primary']")
    wrong_login_warning = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")

    def enter_email(self,text):
        self.type_into_feild(self.Email, text)

    def enter_password(self, text):
        self.type_into_feild(self.Pasword, text)

    def login_button_click(self):
        self.click_on_element(self.login_button)
        return AccountPage(self.driver)

    def wrong_login(self, expected_message):
        return self.check_warning_message(self.wrong_login_warning, expected_message)

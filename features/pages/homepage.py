from selenium.webdriver.common.by import By
from features.pages.basepage import BasePage
from features.pages.loginpage import LoginPage
from features.pages.registerpage import RegisterPage
from features.pages.searchpage import SearchPage


class HomePage(BasePage):

    my_account_css = (By.CSS_SELECTOR, "i[class='fa fa-user']")
    login_button = (By.LINK_TEXT, "Login")

    search_box = (By.NAME, "search")
    search_button = (By.CSS_SELECTOR, "button[class='btn btn-default btn-lg']")

    my_account_button = (By.LINK_TEXT, "My Account")
    register_new_account = (By.LINK_TEXT, "Register")

    def click_on_my_accunt(self):
        self.click_on_element(self.my_account_css)

    def login_to_account(self):
        self.click_on_element(self.login_button)
        return LoginPage(self.driver)

    def my_page_check(self, expected_title):
        return self.verify_page_title(expected_title)

    def search(self, text):
        self.type_into_feild(self.search_box, text)

    def search_button_click(self):
        self.click_on_element(self.search_button)
        return SearchPage(self.driver)

    def enter_to_register(self):
        self.click_on_element(self.my_account_button)
        self.click_on_element(self.register_new_account)
        return RegisterPage(self.driver)

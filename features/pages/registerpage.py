
from selenium.webdriver.common.by import By
from features.pages.basepage import BasePage


class RegisterPage(BasePage):


    # locators
    name_field = (By.ID, "input-firstname")
    last_name_field = (By.ID, "input-lastname")
    email_field = (By.ID, "input-email")
    phone_field = (By.ID, "input-telephone")
    password_field = (By.ID, "input-password")
    confirm_password_field = (By.ID, "input-confirm")

    confirm_policy_button = (By.CSS_SELECTOR, "input[type='checkbox']")
    register_user_button = (By.XPATH, "//input[@value='Continue']")

    # alerts
    warinig_message_locator = (By.XPATH, "//div[@id='content']/h1")
    warinig_duplicated_email_locator = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
    warinig_empty_email_locator = (By.XPATH, "//input[@id='input-firstname']/following::div")

    def register_user(self, name, last_name, email, phone, password, password_confirm):
        self.type_into_feild(self.name_field, name)
        self.type_into_feild(self.last_name_field, last_name)
        self.type_into_feild(self.email_field, email)
        self.type_into_feild(self.phone_field, phone)
        self.type_into_feild(self.password_field, password)
        self.type_into_feild(self.confirm_password_field, password_confirm)

    def register_button_click(self):
        self.click_on_element(self.confirm_policy_button)
        self.click_on_element(self.register_user_button)

    def warinig_message(self, expected_message):
        return self.check_warning_message(self.warinig_message_locator, expected_message)

    def warinig_message_duplicated_email(self, expected_message):
        return self.check_warning_message(self.warinig_duplicated_email_locator, expected_message)

    def warinig_message_empty_form(self, expected_message):
        return self.check_warning_message(self.warinig_empty_email_locator, expected_message)

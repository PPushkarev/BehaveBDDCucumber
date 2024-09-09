from selenium.webdriver.common.by import By
from features.pages.basepage import BasePage


class SearchPage(BasePage):


    search_result = (By.LINK_TEXT, 'HP LP3065')
    invalid_product_result = (By.XPATH, "//input[@id='button-search']//following::p")

    def search_result_displayed(self):
        return self.check_displayed_element(self.search_result)

    def search_invalid_result_displayed(self, expected_message):
        return self.check_warning_message(self.invalid_product_result, expected_message)

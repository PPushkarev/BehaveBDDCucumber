

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def verify_page_title(self, expected_title):
        return self.driver.title.__eq__(expected_title)


    def type_into_feild(self,locator,text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def check_warning_message(self, locator, expected_message):
        actual_message = self.driver.find_element(*locator).text.strip()
        return expected_message in actual_message

    def check_displayed_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()









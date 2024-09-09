import pytest
from features.pages.accountpage import AccountPage
from features.pages.homepage import HomePage
from features.pages.loginpage import LoginPage
from features.pages.registerpage import RegisterPage
from features.pages.searchpage import SearchPage


# анотация типов
class Basetest:
    accountpage: AccountPage
    homepage: HomePage
    loginpage: LoginPage
    registerpage: RegisterPage
    searchpage: SearchPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.accountpage = AccountPage(driver)
        request.cls.homepage = HomePage(driver)
        request.cls.loginpage = LoginPage(driver)
        request.cls.registerpage = RegisterPage(driver)
        request.cls.searchpage = SearchPage(driver)

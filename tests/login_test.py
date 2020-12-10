from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.home_Page import HomePage
from utils import utils as util

@pytest.mark.usefixtures("test_setup")
class Testlogin():


    def test_login(self):
        driver = self.driver
        driver.get(util.URL)
        login = LoginPage(driver)
        login.enter_username(util.USERNAME)
        login.enter_password(util.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == 'OrangeHRM'
        except AssertionError as error:
            print("Assertion error occured")
            print(error)
            raise
        except:
            print("There was an exception")
        else:
            print("No exception occured")
        finally:
            print("I am inside finally")



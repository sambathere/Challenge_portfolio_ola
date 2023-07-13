import os
import unittest
import time

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from selenium import webdriver

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from pages.login_page import LoginPage

from pages.dashboard import Dashboard


#def assert_element_text(driver, xpath, expected_text):
   #element = driver.find_element(by=By.XPATH, value=xpath)
    #element_text = element.text
    #assert expected_text == element_text

class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user05@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        #field_text = assert_element_text(self.driver, "//element_xpath", "Scout Panel")
        time.sleep(5)


    @classmethod
    def tearDown(self):
        self.driver.quit()


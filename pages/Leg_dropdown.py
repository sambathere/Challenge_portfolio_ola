import os
import unittest
import time

from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from pages.login_page import LoginPage

from pages.dashboard import Dashboard


class TestLegDropdown(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_leg_drowpdown(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user05@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        user_login.add_a_player_button()
        user_login.select_leg("Right leg")
        time.sleep(3)
        user_login.select_leg("Left leg")
        time.sleep(3)

        dashboard_page = Dashboard(self.driver)

        time.sleep(10)

    @classmethod
    def tearDown(self):
        self.driver.quit()
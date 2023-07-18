from datetime import time

from pages.base_page import BasePage

import pyautogui

def take_screenshot(Leg_dropdown, screenshott):
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshott)


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver


    login_field_xpath = "//*[@id='login']"
    password_field_xpath = '//*[@id="password"]'
    sign_in_button_xpath = "//div/button/span"
    sign_out_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span'
    add_a_player_button_xpath = "//*/div/a/button"
    name_add_a_player_form_xpath = "//*/div[2]/div/div/input"
    surname_add_a_player_form_xpath = '//*/div/div[3]/div/div/input'
    main_position_add_a_player_form_xpath = '//*/div/div[11]/div/div/input'
    age_add_a_player_form_xpath = '//*/div/div[7]/div/div/input'
    leg_dropdown_xpath = '//*[@id="mui-component-select-leg"]'
    Right_leg_select = '//*[@id="menu-leg"]/div[3]/ul/li[1]'
    Left_leg_select = '//*[@id="menu-leg"]/div[3]/ul/li[2]'
    submit_add_a_player_form_xpath = '//*/form/div[3]/button[1]/span[1]'
    clear_button_xpath = '//*/div[3]/button[2]/span[1]'
    element_xpath = "//*/div//h5"
    DEV_TEAM_CONTACT_button_xpath = '//div[1]/div/div[3]/a/span[1]'
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/login'
    expected_title = 'Scouts panel - sign in'


    def select_leg(self, leg):
        self.click_on_the_element(self.leg_dropdown_xpath)
        if leg == 'Right leg':
            self.click_on_the_element(self.Right_leg_select)
        else:
            self.click_on_the_element(self.Left_leg_select)


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def click_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def add_a_player_button(self):
        self.click_on_the_element(self.add_a_player_button_xpath)

    def type_in_name(self, name):
        self.field_send_keys(self.name_add_a_player_form_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_add_a_player_form_xpath, surname)

    def type_in_main_position(self, position):
        self.field_send_keys(self.main_position_add_a_player_form_xpath, position)

    def type_in_age(self, age):
        self.field_send_keys(self.age_add_a_player_form_xpath, age)

    def submit_add_a_player_form_button(self):
        self.click_on_the_element(self.submit_add_a_player_form_xpath)

    def submit_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)

    def click_DEV_TEAM_CONTACT_button(self):
        self.click_on_the_element(self.DEV_TEAM_CONTACT_button_xpath)



    def title_of_page(self):
        current_title = self.get_page_title(self.login_url)
        print("Aktualny tytuł strony:", current_title)
        assert current_title == self.expected_title


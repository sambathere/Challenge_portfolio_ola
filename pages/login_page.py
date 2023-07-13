import unittest


from pages.base_page import BasePage

class LoginPage(BasePage):

    login_field_xpath = "//*[@id='login']"
    password_field_xpath = '//*[@id="password"]'
    sign_in_button_xpath = "//div/button/span"
    add_a_player_button_xpath = "//*/div/a/button"
    element_xpath = "//*/div//h5"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/login'
    expected_title = 'Scouts panel - sign in'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def add_a_player_button(self):
        self.click_on_the_element(self.add_a_player_button_xpath)


    def title_of_page(self):
        current_title = self.get_page_title(self.login_url)
        print("Aktualny tytuł strony:", current_title)
        assert current_title == self.expected_title


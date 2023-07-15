from lib2to3.pgen2 import driver

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


#add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
#dev_team_contact_button_xpath = "// *[ @ id = '__next'] / div[1] / main / div[3] / div[1] / div / div[3] / a / span[1]"
#Players_button_xpath = "// *[text() = 'Players']"
#Main_page_button_xpath = "// *[text() = 'Main page']"
#Sign_out_button_xpath = "// span[contains(text(), 'Sign out')]"
#Last_created_player = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button"
#Language_button_Polski_xpath = "//span[contains(@class, 'MuiListItemText-primary') and . = 'Polski']"
#Language_button_English_xpath = "//span[contains(@class, 'MuiListItemText-primary') and . = 'English']"
#Last_updated_player_button_path = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1]"
#Last_updated_report_button_path = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]/button/span[1]"


class WebDriverWait:
    pass


class Dashboard(BasePage):

    futbol_kolektyw_logo_xpath = '//*[@title="Logo Scouts Panel"]'
    add_a_player_button_xpath = "//*/div/a/button"
    expected_title = 'Scouts panel - sign in'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en/dashboard'
    Wait = WebDriverWait(driver, 10)


    def title_of_page(self):
      self.wait_for_element_to_be_clickable(self.futbol_kolektyw_logo_xpath)
      assert self.get_page_title(self.dashboard_url) == self.expected_title


    def click_on_the_add_a_player_button(self):
        self.click_on_the_element(self.add_a_player_button_xpath)











from pages.base_page import BasePage



class Dashboard(BasePage):

  add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
  dev_team_contact_button_xpath = "// *[ @ id = '__next'] / div[1] / main / div[3] / div[1] / div / div[3] / a / span[1]"
  Players_button_xpath = "// *[text() = 'Players']"
  Main_page_button_xpath = "// *[text() = 'Main page']"
  Sign_out_button_xpath = "// span[contains(text(), 'Sign out')]"
  Last_created_player = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button"
  Language_button_Polski_xpath = "//span[contains(@class, 'MuiListItemText-primary') and . = 'Polski']"
  Language_button_English_xpath = "//span[contains(@class, 'MuiListItemText-primary') and . = 'English']"
  Last_updated_player_button_path = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1]"
  Last_updated_report_button_path = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]/button/span[1]"

pass

import time

from pages.base_page import BasePage

class Dashboard(BasePage):

    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en/dashboard'
    expected_title = 'Scouts panel - sign in'

    def title_of_page(self):
      time.sleep(4)
      assert self.get_page_title(self.dashboard_url) == self.expected_title













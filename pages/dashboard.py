from pages.base_page import BasePage


class Dashboard(BasePage):

  1  add_player_button_xpath = “//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]”
  2  dev_team_contact_button_xpath = "// *[ @ id = "__next"] / div[1] / main / div[3] / div[1] / div / div[3] / a / span[1]"
  3  Players_button_xpath = "// *[text() = "Players"]"
  4  Main_page_button_xpath = "// *[text() = "Main page"]"
  5  Sign_out_button_xpath = "// span[contains(text(), 'Sign out')]"
  6  Last_created_player = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[1]/button"
  7  Language_button_Polski_xpath = "//span[contains(@class, 'MuiListItemText-primary') and . = 'Polski']"
  8  Language_button_English_xpath = "//span[contains(@class, 'MuiListItemText-primary') and . = 'English']"
  9  Last_updated_player_button_path = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1]"
  10 Last_updated_report_button_path = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[5]/button/span[1]"

pass
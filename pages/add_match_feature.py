from pages.base_page import BasePage


class add_match_feature(BasePage):

    1 Match_at_home_button_xpath = "// span[contains(text(), 'Match at home')]"
    2 Match_out_home_button_xpath = "// span[contains(text(), 'Match out home')]"
    3 Clear_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"
    4 Submit_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]"
    5 Enemy_team_score_field = "//input[@name='enemyTeamScore']"
    6 My_team_score_field = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    7 Time_played_rating = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    8 General_field = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[12]/div/div/input"
    9 Web_match_field = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
    10 Number_rating = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"

pass
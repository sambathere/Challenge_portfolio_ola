from pages.base_page import BasePage


class add_match_feature(BasePage):

    Match_at_home_button_xpath = "// span[contains(text(), 'Match at home')]"
    Match_out_home_button_xpath = "// span[contains(text(), 'Match out home')]"
    Clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"
    Submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]"
    Enemy_team_score_field = "//input[@name='enemyTeamScore']"
    My_team_score_field = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    Time_played_rating = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    General_field = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[12]/div/div/input"
    Web_match_field = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
    Number_rating = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"

pass
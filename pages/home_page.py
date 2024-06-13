from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    LHS_NAVBAR = (By.CSS_SELECTOR, "button.sc-49542412-3.ipGSFC")
    SPORT_LINK = (By.XPATH, "//span[@data-testid='level1NavText-/sport']")

    def open_navbar(self):
        self.click_element(self.LHS_NAVBAR)

    def go_to_sport(self):
        self.click_element(self.SPORT_LINK)

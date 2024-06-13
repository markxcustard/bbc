from selenium.webdriver.common.by import By
from .base_page import BasePage

class SportPage(BasePage):
    FORMULA1_LINK = (By.XPATH, "//span[@class='ssrcss-1u47p8g-LinkTextContainer eis6szr1' and text()='Formula 1']")

    def go_to_formula1(self):
        self.click_element(self.FORMULA1_LINK)

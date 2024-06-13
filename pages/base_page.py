from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Increased wait time for better reliability

    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()

    def find_element(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def get_page_title(self):
        return self.driver.title

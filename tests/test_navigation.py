import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bbc.pages.home_page import HomePage
from bbc.pages.sport_page import SportPage
import time

def setup_driver(browser):
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_argument("--headless")  # Re-enable headless mode for performance
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-translate")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--window-size=1920,1080")

        # Disable images
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Path to the ChromeDriver
        chromedriver_path = "/usr/local/bin/chromedriver"  # Ensure this path is correct
        service = ChromeService(executable_path=chromedriver_path)

        return webdriver.Chrome(service=service, options=chrome_options)
    elif browser == "firefox":
        return webdriver.Firefox()
    elif browser == "safari":
        return webdriver.Safari()
    else:
        raise ValueError("Browser not supported")

@pytest.mark.parametrize("browser", ["chrome", "firefox", "safari"])
def test_navigation(browser):
    driver = setup_driver(browser)
    home_page = HomePage(driver)
    sport_page = SportPage(driver)

    try:
        print("Opening BBC homepage")
        start_time = time.time()
        # Open the BBC homepage
        home_page.open_url("https://www.bbc.com")
        print("BBC homepage opened in {} seconds".format(time.time() - start_time))

        # Explicit wait for the page to load completely
        start_time = time.time()
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("Page loaded in {} seconds".format(time.time() - start_time))

        # Click on the navbar to open it
        try:
            start_time = time.time()
            print("Trying to click the navbar button")
            navbar_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sc-49542412-3.ipGSFC"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", navbar_button)  # Ensure element is in view
            navbar_button.click()
            print("Navbar button clicked in {} seconds".format(time.time() - start_time))
        except TimeoutException as e:
            print("Failed to find the navbar button. Page source for debugging:")
            print(driver.page_source)
            raise e

        # Wait for the navbar to be visible
        start_time = time.time()
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-testid='level1NavText-/sport']"))
        )
        print("Navbar is visible in {} seconds".format(time.time() - start_time))

        # Ensure the element is in view before clicking
        sport_link = driver.find_element(By.XPATH, "//span[@data-testid='level1NavText-/sport']")
        driver.execute_script("arguments[0].scrollIntoView(true);", sport_link)
        start_time = time.time()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='level1NavText-/sport']"))
        )
        print("Sport link clickable in {} seconds".format(time.time() - start_time))
        
        # Navigate to the sport section
        start_time = time.time()
        home_page.go_to_sport()
        print("Navigated to sport section in {} seconds".format(time.time() - start_time))

        # Wait for the sport section to load
        start_time = time.time()
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ssrcss-1u47p8g-LinkTextContainer eis6szr1' and text()='Formula 1']"))
        )
        print("Sport section loaded in {} seconds".format(time.time() - start_time))

        # Navigate to Formula 1 section
        start_time = time.time()
        sport_page.go_to_formula1()
        print("Navigated to Formula 1 section in {} seconds".format(time.time() - start_time))

        # Wait for the Formula 1 section to load
        start_time = time.time()
        WebDriverWait(driver, 20).until(
            EC.url_to_be("https://www.bbc.com/sport/formula1")
        )
        print("Formula 1 section loaded in {} seconds".format(time.time() - start_time))

        # Verify the URL
        assert driver.current_url == "https://www.bbc.com/sport/formula1"
        print("URL verified")
    finally:
        driver.quit()
        print("Browser closed")

import sys
import os
import pytest

# Ensure the bbc directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope="session", autouse=True)
def setup_drivers():
    # Ensure the web drivers are in your PATH or provide the path to the drivers
    # Download drivers from the respective sources:
    # Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
    # Firefox: https://github.com/mozilla/geckodriver/releases
    # Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/
    pass

# BBC Website Automation Project

This project automates navigation and interaction with the BBC website using Selenium and Python. The automation script performs various actions such as opening the homepage, navigating through the left-hand side (LHS) navigation bar, and accessing different sections like Sport and Formula 1.

## Project Structure

bbc/
├── pages/
│ ├── init.py
│ ├── base_page.py
│ ├── home_page.py
│ ├── sport_page.py
├── tests/
│ ├── init.py
│ ├── test_navigation.py
├── init.py
├── conftest.py
├── .gitignore
├── README.md


### Pages

- `base_page.py`: Contains the base class for all page objects.
- `home_page.py`: Contains methods and locators for the BBC homepage.
- `sport_page.py`: Contains methods and locators for the BBC Sport page.

### Tests

- `test_navigation.py`: Contains the test cases for navigating through the BBC website.

## Setup Instructions

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)
- Google Chrome, Mozilla Firefox, and Safari browsers
- ChromeDriver, GeckoDriver (Firefox), and SafariDriver for Selenium

### Installing Dependencies

1. Create a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

2. Install the required Python packages:

pip install -r requirements.txt

Setting Up WebDrivers
ChromeDriver:

Download ChromeDriver from ChromeDriver Downloads and place it in a directory included in your system's PATH.

GeckoDriver:

Download GeckoDriver from GeckoDriver Releases and place it in a directory included in your system's PATH.

SafariDriver:

SafariDriver is included with Safari. To enable it, run the following command:

safaridriver --enable

Running the Tests
To run the tests, use the following command:

pytest bbc/tests/test_navigation.py

.gitignore
The .gitignore file is configured to exclude unnecessary files and directories from the repository, such as bytecode files, virtual environments, and test caches.

Contributing
Feel free to fork this project, make improvements, and submit pull requests. Ensure your code follows the existing coding style and passes all tests.

License
This project is licensed under the MIT License. See the LICENSE file for details.

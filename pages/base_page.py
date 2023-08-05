
from selenium.webdriver.firefox.webdriver import WebDriver


class BasePage:
    base_url = 'https://www.nytimes.com/'
    def __init__(self, driver: WebDriver):
        self.driver = driver


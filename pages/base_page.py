
from selenium.webdriver.firefox.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver


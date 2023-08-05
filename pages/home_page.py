import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


def parse_date(date_text):
    return datetime.datetime.strptime(date_text, "%A, %B %d, %Y")


class HomePage(BasePage):
    CONTINUE_BUTTON = (By.XPATH, '/html/body/div[3]/div/button')
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div/header/section[1]/div[1]/div[2]/button')
    SEARCH_INPUT = (By.XPATH, '/html/body/div[1]/div[2]/div/header/section[1]/div[1]/div[2]/div/form/div/input')
    GO_SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div/header/section[1]/div[1]/div[2]/div/form/button')
    POP_UP_TERMS = (By.XPATH, '/html/body/div[3]/div')
    GDPR_ACCEPT = (By.XPATH, '/html/body/div[1]/div[3]/main/div[2]/div[2]/div/div[2]/button[1]')
    RESULT_SEARCH = (By.ID, 'app')
    SHOW_COUNT = (By.XPATH, '/html/body/div/div[2]/main/div/div[1]/div[1]/p')
    BUSINESS_SECTION = (By.XPATH, '/html/body/div[1]/div[2]/div/header/div[4]/ul/li[5]')
    DATE_TEXT = (By.XPATH, '/html/body/div[1]/div[2]/div/header/section[2]/div[1]/div[1]/span')

    def terms_handler(self):
        continue_button = self.driver.find_element(*self.CONTINUE_BUTTON)
        continue_button.click()

    def pop_up_wait(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.POP_UP_TERMS))

    def gdpr_accept(self):
        accept = self.driver.find_element(*self.GDPR_ACCEPT)
        accept.click()

    def click_search_button(self):
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()

    def search(self):
        word_to_check = 'Crypto'
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(word_to_check)
        go_search = self.driver.find_element(*self.GO_SEARCH_BUTTON)
        go_search.click()

    def business_section_link(self):
        business = self.driver.find_element(*self.BUSINESS_SECTION)
        business.click()

    def check_date(self):
        date_text = self.driver.find_element(*self.DATE_TEXT).text
        date_on_site = parse_date(date_text)
        current_date = datetime.datetime.now().date()
        assert date_on_site.date() >= current_date
# тут я не разобрался как вынести assert в файл с тестами

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):
    # Определите локаторы элементов на домашней странице
    CONTINUE_BUTTON = (By.XPATH, '/html/body/div[3]/div/button')
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div/header/section[1]/div[1]/div[2]/button')
    SEARCH_INPUT = (By.XPATH, '/html/body/div[1]/div[2]/div/header/section[1]/div[1]/div[2]/div/form/div/input')
    GO_SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div/header/section[1]/div[1]/div[2]/div/form/button')
    POP_UP_TERMS = (By.XPATH, '/html/body/div[3]/div')
    GDPR_ACCEPT = (By.XPATH, '/html/body/div[1]/div[3]/main/div[2]/div[2]/div/div[2]/button[1]')
    RESULT_SEARCH = (By.ID, 'app')
    SHOW_COUNT = (By.XPATH, '/html/body/div/div[2]/main/div/div[1]/div[1]/p')

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

    def search(self, query):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(query)

    def go_search(self):
        go_search = self.driver.find_element(*self.GO_SEARCH_BUTTON)
        go_search.click()

    def result_search(self):
        search_result = self.driver.find_element(*self.RESULT_SEARCH)
        return search_result.text.lower()

    def print_result(self):
        article_count = self.driver.find_element(*self.SHOW_COUNT)
        article_count.text



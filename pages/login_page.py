from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

from pages.base_page import BasePage


def generate_email():
    username = "test" + ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 5)))
    domain = "gmail.com"
    email = f"{username}@{domain}"
    return email


def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


class LoginPage(BasePage):
    CONTINUE_BUTTON = (By.XPATH, '/html/body/div[3]/div/button')
    LOGIN_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div/header/section[1]/div[4]/a[2]')
    EMAIL_INPUT = (By.ID, 'email')
    CONTINUE_ON_LOGIN = (By.XPATH, '/html/body/div/div/div/div/form/div/div[4]/button')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    CREATE_ACCOUNT = (By.XPATH, '/html/body/div/div/div/form/div/div[2]/button')
    CONTINUE_WITHOUT_SUBS = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[2]/a')
    NO_THANKS_BUTTON = (By.XPATH, '/html/body/div/div/div/div/div/button[1]')
    MAYBE_LATER_BUTTON = (By.XPATH, '/html/body/div/div/div/div/button')
    BACK_TO_READ = (By.XPATH, '/html/body/div/div/div/div/button')
    AUTH_ACCOUNT_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div/header/section[1]/div[4]/div[1]/button')

    def terms_handler(self):
        continue_button = self.driver.find_element(*self.CONTINUE_BUTTON)
        continue_button.click()

    def login_button_wait(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_BUTTON))

    def auth_user_or_not(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        return login_button

    def login_button_click(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()

    def input_email_and_continue(self):
        generated_email = generate_email()
        email = self.driver.find_element(*self.EMAIL_INPUT)
        email.send_keys(generated_email)
        continue_login_button = self.driver.find_element(*self.CONTINUE_ON_LOGIN)
        continue_login_button.click()

    def input_password(self):
        generated_password = generate_password()
        password = self.driver.find_element(*self.PASSWORD_INPUT)
        password.send_keys(generated_password)

    def create_account(self):
        ca = self.driver.find_element(*self.CREATE_ACCOUNT)
        ca.click()

    def continue_without_subs(self):
        cws = self.driver.find_element(*self.CONTINUE_WITHOUT_SUBS)
        cws.click()

    def no_thanks_button(self):
        ntb = self.driver.find_element(*self.NO_THANKS_BUTTON)
        ntb.click()

    def maybe_later_button(self):
        mlb = self.driver.find_element(*self.MAYBE_LATER_BUTTON)
        mlb.click()

    def back_to_read(self):
        btr = self.driver.find_element(*self.BACK_TO_READ)
        btr.click()

    def account_is_exist(self):
        account = self.driver.find_element(*self.AUTH_ACCOUNT_BUTTON)
        return account





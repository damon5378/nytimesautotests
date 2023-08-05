
from pages.login_page import LoginPage
from pages.base_page import BasePage


def test_auth_user_or_not(driver):
    login_page = LoginPage(driver)
    driver.get(BasePage.base_url)

    login_page.terms_handler()
    login_page.login_button_wait()

    assert login_page.auth_user_or_not(), "User is not authenticated"


def test_login(driver):
    login_page = LoginPage(driver)
    driver.get(BasePage.base_url)
    login_page.terms_handler()
    login_page.login_button_wait()
    login_page.login_button_click()
    login_page.input_email_and_continue()
    driver.implicitly_wait(3)
    login_page.input_password()
    driver.implicitly_wait(3)
    login_page.create_account()
    login_page.continue_without_subs()
    login_page.no_thanks_button()
    login_page.maybe_later_button()
    login_page.back_to_read()

    assert login_page.account_is_exist(), "User is auth"



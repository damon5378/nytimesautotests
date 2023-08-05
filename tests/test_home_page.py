import time
from pages.home_page import HomePage
from pages.base_page import BasePage


def test_search_on_home_page(driver):
    home_page = HomePage(driver)

    home_page.driver.get(BasePage.base_url)

    home_page.pop_up_wait()
    home_page.terms_handler()
    home_page.gdpr_accept()
    home_page.click_search_button()
    home_page.search()

    assert "Crypto" in driver.title


def test_home_page_title(driver):
    driver.get(BasePage.base_url)
    check_title = 'The New York Times - Breaking News, US News, World News and Videos'
    assert check_title in driver.title, "Заголовок домашней страницы некорректен."


def test_business_section_link(driver):
    home_page = HomePage(driver)
    driver.get(BasePage.base_url)
    home_page.pop_up_wait()
    home_page.terms_handler()
    home_page.business_section_link()
    assert "Business" in driver.title, "Ссылка на раздел 'Бизнес' не работает."


def test_date_compare(driver):
    home_page = HomePage(driver)
    driver.get(BasePage.base_url)
    home_page.pop_up_wait()
    home_page.terms_handler()
    home_page.check_date()




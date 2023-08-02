# test_home_page.py
import time

from pages.home_page import HomePage


def test_search_on_home_page(driver):
    # Инициализируем страницу
    home_page = HomePage(driver)

    # Открываем домашнюю страницу
    home_page.driver.get('https://www.nytimes.com/')

    # Выполняем действия на странице и проверяем результаты
    time.sleep(5)
    # driver.implicitly_wait(10)
    # home_page.pop_up_wait()
    home_page.terms_handler()
    # home_page.gdpr_accept()
    home_page.click_search_button()
    home_page.search('Crypto')
    home_page.go_search()

    # Здесь добавьте дополнительные проверки, которые вы хотите выполнить на результате поиска
    # Например, можно убедиться, что результаты поиска содержат ключевое слово 'Python'.
    # assert 'Crypto' in home_page.result_search(), "A word - Crypto was found on the page"
    print(home_page.print_result())
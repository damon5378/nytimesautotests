from selenium import webdriver
import pytest
import requests

API_KEY = "3iElcEAbAjbQuSzc3jRJtU8JVTnA7x5g"  # Замените на свой API ключ

BASE_URL_API = "https://api.nytimes.com/svc/"


@pytest.fixture()
def driver():
    ff_driver = webdriver.Firefox()
    yield ff_driver


@pytest.fixture(scope="session")
def api_key():
    return API_KEY


@pytest.fixture(scope="session")
def api_base_url():
    return BASE_URL_API


@pytest.fixture(scope="session")
def session():
    return requests.Session()

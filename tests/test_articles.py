# api_tests/articles.py

import pytest


class TestArticlesAPI:

    @property
    def endpoint(self):
        return "search/v2/articlesearch.json"

    def test_get_articles(self, session, api_key, api_base_url):
        params = {
            "api-key": api_key,
            "q": "Crypto",  # Замените на свой запрос
            "sort": "newest"
        }
        response = session.get(f"{api_base_url}{self.endpoint}", params=params)

        assert response.status_code == 200
        assert "response" in response.json()
        assert "docs" in response.json()["response"]

    def test_get_articles_with_invalid_query(self, session, api_key, api_base_url):
        params = {
            "api-key": api_key,
            "q": "",
        }
        response = session.get(f"{api_base_url}{self.endpoint}", params=params)

        assert response.status_code == 400
        assert "message" in response.json()

    def test_get_second_page_of_articles(self, session, api_key, api_base_url):
        params = {
            "api-key": api_key,
            "q": "Crypto",
            "sort": "newest",
            "page": 2
        }
        response = session.get(f"{api_base_url}{self.endpoint}", params=params)

        assert response.status_code == 200
        assert "response" in response.json()
        assert "docs" in response.json()["response"]



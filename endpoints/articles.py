# api_tests/articles.py

import pytest


class TestArticlesAPI:
    @property
    def endpoint(self):
        return "search/v2/articlesearch.json"

    def test_get_articles(self, session, api_key, api_base_url):
        params = {
            "api-key": api_key,
            "q": "Python",
            "sort": "newest"
        }
        response = session.get(f"{api_base_url}{self.endpoint}", params=params)

        assert response.status_code == 200
        assert "response" in response.json()
        assert "docs" in response.json()["response"]



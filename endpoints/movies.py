# api_tests/movies.py

import pytest

class TestMoviesAPI:

    @property
    def endpoint(self):
        return "movies/v2/reviews/search.json"

    def test_get_movies(self, session, api_key, api_base_url):
        params = {
            "api-key": api_key,
            "query": "Spider-Man",  # Замените на свой запрос
        }
        response = session.get(f"{api_base_url}{self.endpoint}", params=params)

        assert response.status_code == 200
        assert "results" in response.json()

    # Добавьте дополнительные тесты, если необходимо

# api_tests/movies.py

import pytest


class TestMoviesAPI:

    @property
    def endpoint(self):
        return "movies/v2/reviews/search.json"

    def test_get_movies(self, session, api_key, api_base_url):
        params = {
            "api-key": api_key,
            "query": "Spider-Man",
        }
        response = session.get(f"{api_base_url}{self.endpoint}", params=params)

        assert response.status_code == 200
        assert "results" in response.json()

    def test_get_movies_with_invalid_query(self, session, api_key, api_base_url):
        params = {
            "api-key": api_key,
            "query": "",
        }
        response = session.get(f"{api_base_url}{self.endpoint}", params=params)

        assert response.status_code == 400
        assert "fault" in response.json()

    def test_get_second_page_of_movies(self, session, api_key, api_base_url):
        params = {
            "api-key": api_key,
            "query": "Spider-Man",
            "offset": 20,
        }
        response = session.get(f"{api_base_url}{self.endpoint}", params=params)

        assert response.status_code == 200
        assert "results" in response.json()

    def test_search_with_invalid_rating(self, session, api_key, api_base_url):
        params = {
            "api-key": api_key,
            "query": "Spider-Man",
            "mpaa_rating": "invalid_rating",
        }
        response = session.get(f"{api_base_url}{self.endpoint}", params=params)

        assert response.status_code == 400
        assert "fault" in response.json()

    def test_search_with_empty_result(self, session, api_key, api_base_url):
        params = {
            "api-key": api_key,
            "query": "SomeRandomMovieTitle",
        }
        response = session.get(f"{api_base_url}{self.endpoint}", params=params)

        assert response.status_code == 200
        assert "results" in response.json()
        assert len(response.json()["results"]) == 0

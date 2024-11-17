import requests
from config import SEARCH_API_KEY

class SearchAPI:
    def __init__(self):
        self.api_key = SEARCH_API_KEY
        self.url = "https://api.search.com"

    def search(self, query):
        params = {"api_key": self.api_key, "q": query}
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            return response.json()["results"]
        else:
            return []

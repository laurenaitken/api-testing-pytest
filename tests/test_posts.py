import requests
from config import BASE_URL


def test_get_single_post_returns_200():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

import logging
import requests
from config import BASE_URL

logger = logging.getLogger(__name__)


def test_get_single_post_returns_200():
    logger.info(f"Making a GET request to {BASE_URL}/posts/1")
    response = requests.get(f"{BASE_URL}/posts/1")

    logger.info(f"Response status code: {response.status_code}")
    assert response.status_code == 200

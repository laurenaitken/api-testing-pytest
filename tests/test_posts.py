import requests

# Create base URL variable to allow for easier test expansion
base_url = "https://jsonplaceholder.typicode.com"

def test_get_single_post_returns_200():

    # Check status code passes before running any further tests
    response = requests.get(f"{base_url}/posts/1")

    # Assert the response status code is 200 OK
    assert response.status_code == 200
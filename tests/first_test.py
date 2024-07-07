import requests
import pytest

# Define base URL
url = "https://cat-fact.herokuapp.com"


# Test function for valid requests
@pytest.mark.parametrize(
    "test_input",
    [{"animal_type": "cat", "amount": "1"}, {"animal_type": "cat", "amount": "500"}],
)
def test_cat_app_valid(test_input):
    response = requests.get(f"{url}/facts/random", params=test_input)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    # Additional assertions can be added here based on the expected response


@pytest.mark.parametrize("test_input", [{"animal_type": "cat", "amount": "501"}])
def test_cat_app_high_boundary(test_input):
    response = requests.get(f"{url}/facts/random", params=test_input)

    assert response.message == "Limited to 500 facts at a time"
    assert response.status_code != 200


@pytest.mark.parametrize(
    "test_input",
    [
        {"animal_type": "cat", "amount": "0"},
    ],
)
def test_cat_app_low_boundary(test_input):
    response = requests.get(f"{url}/facts/random", params=test_input)

    assert response.status_code == 200
    assert response.json() == []

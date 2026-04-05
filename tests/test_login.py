import pytest
from utils.api_client import login
from utils.data_loader import load_test_data

@pytest.mark.parametrize("data", load_test_data())
def test_login_data_driven(data):
    response = login({"email": data["email"], "password": data["password"]})
    assert response.status_code == data["expected_status"]
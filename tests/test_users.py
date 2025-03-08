import pytest
import logging
from api.users_api import UsersAPI
from schemas import UserListResponse

# Configure logging
logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def users_api():
    logger.info("Initializing Users API")
    return UsersAPI("https://reqres.in/api")


def test_get_users(users_api):
    logger.info("Executing test: test_get_users")
    response = users_api.get_users()

    logger.info(f"Response Status Code: {response.status_code}")
    logger.debug(f"Response JSON: {response.json()}")

    assert response.status_code == 200
    validated_data = UserListResponse(**response.json())
    assert validated_data.total > 0


def test_create_user(users_api):
    user_data = {
        "name": "Vikram",
        "job": "Automation Engineer"
    }
    logger.info(f"Executing  test: test_create_user with data: {user_data}")

    response = users_api.create_user(user_data)
    print(response)
    logger.info(f"Response Status Code: {response.status_code}")
    logger.debug(f"Response JSON: {response.json()}")

    assert response.status_code == 201
    assert response.json()["name"] == "Vikram"

def test_get_user_by_id(users_api):
    logger.info("Fetching user by ID: 2")
    response = users_api.get_user_by_id(2)
    assert response.status_code == 200
    assert "data" in response.json()

def test_get_invalid_user(users_api):
    logger.info("Fetching non-existent user by ID: 9999")
    response = users_api.get_user_by_id(9999)
    assert response.status_code == 404

def test_create_user_missing_fields(users_api):
    user_data = {"name": "TestUser"}  # Missing job field
    logger.info(f"Creating user with incomplete data: {user_data}")
    response = users_api.create_user(user_data)
    assert response.status_code == 201

def test_delete_user(users_api):
    logger.info("Deleting user with ID: 2")
    response = users_api.delete_user(2)
    assert response.status_code == 204

def test_get_users_pagination(users_api):
    logger.info("Fetching paginated users data")
    response = users_api.get_users()
    assert response.status_code == 200
    json_data = response.json()
    assert "page" in json_data and "per_page" in json_data

def test_create_multiple_users(users_api):
    users = [
        {"name": "Alice", "job": "Developer"},
        {"name": "Bob", "job": "Tester"}
    ]
    for user in users:
        logger.info(f"Creating user: {user}")
        response = users_api.create_user(user)
        assert response.status_code == 201

def test_response_time(users_api):
    logger.info("Checking API response time")
    response = users_api.get_users()
    assert response.elapsed.total_seconds() < 2, "API response time is too slow"

def test_content_type(users_api):
    logger.info("Validating API response Content-Type")
    response = users_api.get_users()
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

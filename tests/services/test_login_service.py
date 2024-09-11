import pytest

from services.login_service import LoginService

@pytest.fixture
def login_service():
    return LoginService()

def test_login_success(login_service):
    username = "admin"
    password = "<PASSWORD>"
    assert login_service.login(username, password) == True

def test_login_invalid_username(login_service):
    username = "invalid_user"
    password = "<PASSWORD>"
    assert login_service.login(username, password) == False

def test_login_invalid_password(login_service):
    username = "admin"
    password = "wrong_password"
    assert login_service.login(username, password) == False


def test_login_invalid_credentials(login_service):
    username = "invalid_user"
    password = "wrong_password"
    assert login_service.login(username, password) == False


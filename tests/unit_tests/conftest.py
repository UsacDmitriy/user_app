import pytest

from app.services.user import UserService


@pytest.fixture
def _profile_infos():
    val = {
        0:
            {
                "short_description": "My bio description",
                "long_bio": "This is our long bio",
            },
    }

    return val


@pytest.fixture
def _user_contents():
    val = {
        0:
            {
                "name": "Malik",
                "liked_posts": [1, 2],
            },
    }
    return val

@pytest.fixture
def user_service(_profile_infos, _user_contents):
    user_service = UserService(_profile_infos, _user_contents)
    return user_service


@pytest.fixture(scope="class", autouse=True)
def testing_fixture():
    print("Initializing fixture")
    yield "a"
    print("teardown stuff")

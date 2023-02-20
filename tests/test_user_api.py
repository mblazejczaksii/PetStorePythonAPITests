from http import HTTPStatus
from endpoints_functions.user_api_helpers import post_create_user



def test_create_user():
    assert post_create_user.status_code == HTTPStatus.OK
    print(post_create_user)



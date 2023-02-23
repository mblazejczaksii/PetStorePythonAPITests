from http import HTTPStatus
from endpoints_functions.user_api_helpers import post_create_user, new_user_body

post_response = post_create_user(user=new_user_body)


def test_create_user_status_code():
    assert post_response.status_code == HTTPStatus.OK


def test_create_user_headers():
    assert post_response.headers['Access-Control-Allow-Methods'] == 'GET, POST, DELETE, PUT'


def test_create_user_url():
    assert post_response.url == 'https://petstore.swagger.io/v2/user'

import pytest
import requests

request_common_url = "https://petstore.swagger.io/v2/user"


## Endpoints functions ##
def post_create_user(new_user_body):
    return requests.post(request_common_url, json=new_user_body)


## Fixtures ##
@pytest.fixture()
def new_user_body():
    yield {
          "username": "Mtest",
          "firstName": "Mtest",
          "lastName": "Mtest",
          "email": "mtest@op.com",
          "password": "mtest",
          "phone": "111222333",
          "userStatus": 1
    }
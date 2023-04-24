from http import HTTPStatus
from endpoints_functions import pet_endpoints


def test_place_an_order_for_a_pet_verify_status_code():
    """
    Test: Place an order for a new pet, check status code
    method: POST
    endpoint: https://petstore.swagger.io/v2/store/order
    """
    response = pet_endpoints.order_a_pet()[0]
    assert response.status_code == HTTPStatus.OK


def test_find_purchase_order_by_id_verify_status_code():
    """
    Test: Find purchase order by ID, check status code
    method: GET
    endpoint: http://petstore.swagger.io/v2/store/order/{orderId}
    """
    response = pet_endpoints.purchase_order_by_id()[0]
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_find_purchase_order_by_id_verify_jsons_equality():
    """
    Test: Find purchase order by ID, check if jsons are equal
    method: POST
    method: GET
    endpoint: http://petstore.swagger.io/v2/store/order/{orderId}
    """
    ordered_pet_json = pet_endpoints.order_a_pet()[1]
    response = pet_endpoints.purchase_order_by_id()[1]
    assert response == ordered_pet_json


def test_find_purchase_order_by_id_invalid_order_id_verify_status_code():
    """
    Test: Find purchase order by invalid ID (greater than 10), check status code
    method: GET
    endpoint: http://petstore.swagger.io/v2/store/order/{orderId}
    """
    response = pet_endpoints.purchase_order_with_invalid_id()
    assert response.status_code == HTTPStatus.OK


def test_delete_purchase_order_by_id_verify_status_code():
    """
    Test: Delete purchase order by ID, check status code
    method: DELETE
    endpoint: http://petstore.swagger.io/v2/store/order/{orderId}
    """
    response = pet_endpoints.delete_purchase_order_by_id()
    assert response.status_code == HTTPStatus.OK


def test_delete_purchase_order_with_invalid_id_verify_status_code():
    """
    Test: Delete purchase order with invalid ID, check status code
    method: DELETE
    endpoint: http://petstore.swagger.io/v2/store/order/{orderId}
    """
    response = pet_endpoints.delete_purchase_order_with_invalid_id()
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_purchase_order_with_invalid_id_verify_message_text():
    """
    Test: Delete purchase order with invalid ID, check message
    method: DELETE
    endpoint: http://petstore.swagger.io/v2/store/order/{orderId}
    """
    response = pet_endpoints.delete_purchase_order_with_invalid_id()
    assert response.json()['message'] == 'Order Not Found'

from endpoints_functions.helpers import Pet, Order
import names
import random
import requests

endpoint = 'https://petstore.swagger.io/v2/pet'
order_endpoint = 'https://petstore.swagger.io/v2/store/order'
generated_name = names.get_first_name()
pet_to_add = Pet(name=generated_name).create_pet()
status = random.choice(['available', 'pending', 'sold'])
my_stored_pet_json = []
created_order = Order().create_an_order()


def add_new_pet():
    added_pet = requests.post(url=endpoint, json=pet_to_add)
    pet_json = added_pet.json()
    pet_id = pet_json['id']
    pet_name = pet_json['name']
    my_stored_pet_json.clear()
    my_stored_pet_json.append(pet_json)
    return added_pet, str(pet_id), pet_name, pet_json


def find_pet_by_id():
    pet_id = add_new_pet()[1]
    founded_pet = requests.get(url=endpoint + '/' + pet_id)
    return founded_pet


def find_pet_by_status():
    found_pet_by_status = requests.get(url=endpoint + f"/findByStatus?status={status}")
    return found_pet_by_status


def update_a_pet_with_form_data():
    pet_id = add_new_pet()[1]
    pet_name = names.get_first_name()
    updated_pet = requests.post(url=endpoint + '/' + pet_id, data=f"name={pet_name}&status{status}")
    return updated_pet


def update_an_existing_pet():
    pet_json = add_new_pet()[3]
    pet_json.update({"status": status})
    pet_json.update({"name": names.get_first_name()})
    updated_existing_pet = requests.put(url=endpoint, json=pet_json)
    return updated_existing_pet


def delete_a_pet():
    pet_id = add_new_pet()[1]
    deleted_pet = requests.delete(url=endpoint + '/' + pet_id)
    return deleted_pet


def order_a_pet():
    ordered_pet = requests.post(url=order_endpoint, json=created_order)
    ordered_pet_json = ordered_pet.json()
    ordered_pet_id = ordered_pet_json['id']
    return ordered_pet, ordered_pet_json, str(ordered_pet_id)


def purchase_order_by_id():
    order_id = order_a_pet()[2]
    purchased_order = requests.get(url=order_endpoint + '/' + order_id)
    purchased_order_json = purchased_order.json()
    return purchased_order, purchased_order_json


def purchase_order_with_invalid_id():
    order_id = '123456789'
    order_with_invalid_id = requests.get(url=order_endpoint + '/' + order_id)
    return order_with_invalid_id


def delete_purchase_order_by_id():
    order_id = order_a_pet()[2]
    delete_purchased_order = requests.delete(url=order_endpoint + '/' + order_id)
    return delete_purchased_order


def delete_purchase_order_with_invalid_id():
    order_id = '123456789'
    delete_purchased_order = requests.delete(url=order_endpoint + '/' + order_id)
    return delete_purchased_order

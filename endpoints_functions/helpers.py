import datetime
import random


def generate_id():
    generated_id = random.randint(1000000, 9999999)
    return generated_id


def generate_order_id():
    generated_order_id = random.randint(11, 100)
    return generated_order_id


def generate_category_name():
    category_name_list = ['dog', 'cat', 'fish', 'turtle', 'snake']
    category_name = random.choice(category_name_list)
    return category_name


def generate_tags_name():
    tags_name_list = ['wild', 'pet']
    tags_name = random.choice(tags_name_list)
    return tags_name


def generate_pets_quantity():
    pets_quantity = random.randint(1, 100)
    return pets_quantity


def generate_order_status():
    orders = ('ordered', 'available', 'unavailable', 'pending', 'sent')
    return random.choice(orders)


def ship_date():
    ship_date = datetime.date.today()
    return str(ship_date)


bool_values = (True, False)


# class to create a pet with category_name, name and tags_name and random_id
class Pet:
    def __init__(self, name):
        self.name = name

    def create_pet(self):
        basic_pet = {
            "id": generate_id(),
            "category": {
                "id": generate_id(),
                "name": generate_category_name()
            },
            "name": self.name,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": generate_id(),
                    "name": generate_tags_name()
                }
            ],
            "status": "available"
        }
        return basic_pet


class Order:
    def __init__(self):
        print("Order object created")

    def create_an_order(self):
        created_order = {
            "id": generate_order_id(),
            "petId": generate_id(),
            "quantity": generate_pets_quantity(),
            "shipDate": ship_date(),
            "status": generate_order_status()
        }
        return created_order

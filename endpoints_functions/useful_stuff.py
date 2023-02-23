# simple id generator
import random



def generate_id():
    generated_id = random.randint(1000000, 9999999)
    return generated_id


# class to create a pet with category_name, name and tags_name and random_id
class Pet:
    def __init__(self, category_name, name, tags_name):
        self.category_name = category_name
        self.name = name
        self.tags_name = tags_name

    def create_pet(self):
        basic_pet = {
            "id": generate_id(),
            "category": {
                "id": generate_id(),
                "name": self.category_name
            },
            "name": self.name,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": generate_id(),
                    "name": self.tags_name
                }
            ],
            "status": "available"
        }
        return basic_pet

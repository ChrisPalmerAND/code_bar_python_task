import random
from faker import Faker

def create_data(number_of_people):
    fake = Faker()
    
    collection_of_people = []
    for i in range(number_of_people):
        name = fake.name()
        age = random.randint(0,150)
        height = random.randint(0,250)
        number_of_siblings = random.randint(0, 5)
        homeowner = bool(random.getrandbits(1))
        pets = random.choice(["Dog", "Cat", "Horse", "Gerbil", "Rabbit", "Hamster", "Fish", "None" ])

        person = {
            "age": age,
            "name": name,
            "height": height,
            "homeowner": homeowner,
            "pets": pets,
            "number_of_children": number_of_siblings,
        }

        collection_of_people.append(person)


    return collection_of_people
    
    




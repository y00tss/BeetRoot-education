import random


class Dog():
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.age_factor * self.dog_age


def randon_dog_age():
    return random.randint(0, 15)


age = randon_dog_age()


dog_barny = Dog(age)
result = dog_barny.human_age()


match age:
    case 1:
        print(f"Собаке по имени Барни {age} год. В переводе на человеческие = {result}")
    case 2 | 3 | 4:
        print(f"Собаке по имени Барни {age} года. В переводе на человеческие = {result}")
    case _:
        print(f"Собаке по имени Барни {age} лет. В переводе на человеческие = {result}")
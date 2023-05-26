import random


class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + last_name
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.first_name}, my surname is {self.last_name}, and I`m {str(self.age)} years old")


def print_random_name():
    first = ""
    for _ in range(10):
        random_number = random.randint(97, 122)
        first = first + chr(random_number)
    return first


def print_random_surname():
    last = ""
    for _ in range(10):
        random_number = random.randint(97, 122)
        last = last + chr(random_number)
    return last


def print_age():
    age = random.randint(1, 100)
    return age


person1 = Person(print_random_name().title(), print_random_surname().title(), print_age())
person2 = Person(print_random_name().title(), print_random_surname().title(), print_age())
person3 = Person(print_random_name().title(), print_random_surname().title(), print_age())

person1.talk()
person2.talk()
person3.talk()

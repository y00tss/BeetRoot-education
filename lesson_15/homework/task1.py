class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def say(self):
        print(f"My {self.color} dog '{self.name}' say 'Woof'")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def say(self):
        print(f"My {self.color} cat '{self.name}' say 'Meow'")


def main():
    user_answer = input('What animal do you want to create? (dog/cat): ').lower()
    return user_answer



choose = main()

if choose == 'dog':
    answer = Dog(input("Enter dog's name: ").title(), input("Enter dog's color: ").lower())
    answer.say()
elif choose == 'cat':
    answer = Cat(input("Enter cat's name: ").title(), input("Enter cat's color: ").lower())
    answer.say()
else:
    print('Wrong input! Only dogs and cats are available')
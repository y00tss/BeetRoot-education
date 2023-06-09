import re


class MyClass:
    def __init__(self, email):
        self.email = self.validate(email)
        print(self.email)

    @staticmethod
    def validate(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if re.match(pattern, email):
            return f'Email {email} is correct'
        else:
            return f"Invalid email format"


user_email = input("Enter your email: ")
mail = MyClass(user_email)



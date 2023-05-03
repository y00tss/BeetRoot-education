# Ukrainian phone number
"""Main parameter in task was "10 digits, I changed the condition for easy input and didn't lose the purpose"""

country_code = input("Select your country: \nUkraine - 1, another country - 2 \nYour Answer: ")

if "1" in country_code:
    while True:
        user_number = input("+380 ")
        if user_number.isdigit() and len(user_number) == 9:
            print("Number is right")
            break
        elif user_number.isalpha():
            print("The entered number must include only numbers! Try again!")
            continue
        elif user_number.isdigit() and len(user_number) != 9:
            print("You must enter a 9 digit number. Try again")
            continue
        else:
            print("Wrong number! Try again!")
            continue
else:
    print("Next step only for ukrainian")


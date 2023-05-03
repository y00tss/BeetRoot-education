import random

random_number = random.randint(1, 10)

# exmp
print(random_number)



i = 0
while i < 5:
    user_answer = int(input("I guessed a number from 1 for 10. Try to guess it: "))
    if user_answer == random_number:
        print("Yes, your right")
        break
    elif user_answer < random_number:
        print("Your number is smaller, than mine")
        i += 1
    elif user_answer > random_number:
        print("Your number is bigger, than mine")
        i += 1



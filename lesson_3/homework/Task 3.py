# additional

import time
import random
digit1 = random.randint(0, 100)
digit2 = random.randint(0, 100)
result = digit1 + digit2

# introducing of program

print("""
Hello! Its math quiz! I will show you a expression and you should to answer. You have 3 trying\nAre you ready?""")
time.sleep(3)                                                                                                           # timing for next step
print("Lets go")
time.sleep(1)                                                                                                           # timing for next step


i = 0
while i < 3:                                                                                                            # while for only 3 trying
    answer = int(input(f"{digit1} + {digit2} = "))                                                                      # user answer with expression, using random digits for 0 till 100
    if result == answer:
        print("Yes, your right")
        break                                                                                                           # stop the program if user`s answer is correct
    else:
        i += 1
        if i == 3:
            print("You lose")
        else:
            print("Wrong answer, You have", 3 - i, "trying!")                                                           # additional info about counting of trying
print("Thank you!")                                                                                                     # in any case will show "thx"




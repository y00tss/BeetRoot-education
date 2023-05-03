import random

low = int(input("Low limit : "))
high = int(input("High limit : "))
max_num = 0                                                                                                             # this program doesn't work with negative numbers ! ! !

i = 0
while i < 10:
    random_num = random.randint(low, high)                                                                              # in task don`t have info about limits, so I offer this program ask low and high litit from user
    if random_num > max_num:
        max_num = random_num
    i += 1
print(max_num)
import random
list1 = []
list2 = []

i = 0
while i < 10:
    list1.append(random.randint(1, 10))
    list2.append(random.randint(1, 10))
    i += 1

result = list1 + list2
sets = set(result)
result = list(sets)
print(result)




def with_index(iterable, start=0):
    index = 1
    for value in enumerate(iterable, start):
        yield value
        index += 1


a = with_index(["Vova", "Vlad", "Masha", "Katya"], 1)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
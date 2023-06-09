def in_range(start, end, step=1):
    for i in range(start, end, step):
        yield i


a = in_range(1, 10, 2)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


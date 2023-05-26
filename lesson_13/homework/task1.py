

def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} called with {args}")
        return func(*args)

    return wrapper
@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(5, 5)
scn = square_all(5, 8, 9, 10)
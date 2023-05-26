def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    print(f"Invalid argument type: {arg} is not of type {type_}.")
                    return False
                if len(arg) > max_length:
                    print(f"Length is bigger, that {max_length}. Result - False.")
                    return False

                for symbol in contains:
                    if symbol not in arg:
                        print(f"Dont have a required symbol: {symbol}.")
                        return False
            return func(*args)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

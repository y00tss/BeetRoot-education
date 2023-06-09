from functools import wraps


class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return int(result)

        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)

        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                if result.lower() == 'true':
                    return True
                elif result.lower() == 'false':
                    return False
            return result

        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return float(result)

        return wrapper


@TypeDecorators.to_int
def do_int(string: str):
    return string


@TypeDecorators.to_bool
def do_bool(string: str):
    return string


@TypeDecorators.to_str
def do_str(string: str):
    return string


@TypeDecorators.to_float
def do_float(string: str):
    return string


assert do_int('25') == 25
assert do_bool('True') is True
assert do_str(25) == '25'
assert do_float('25.5') == 25.5

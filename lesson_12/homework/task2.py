def stop_words(words):
    def decorator(func):
        def wrapper(*args, **kwargs):
            slogan = func(*args, **kwargs)
            for word in words:
                slogan = slogan.replace(word, '*')
            return slogan
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

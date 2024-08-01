
# 1. Stringni katta harflarga o'tkazadigan dekorator
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() if isinstance(result, str) else result
    return wrapper
@uppercase_decorator
def greet(name):
    return f"Salom, {name}!"
print(greet("Ali"))
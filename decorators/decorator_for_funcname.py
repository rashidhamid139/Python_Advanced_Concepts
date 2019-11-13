from functools import wraps, partial

def debug(func=None, *, prefix=''):
    if func is None:
        return partial(debug, prefix=prefix)
    msg = prefix + func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper





@debug(prefix = "I am calling: ")
def add(x,y):
    return x+y

@debug(prefix = "I am calling: ")
def sub(x,y):
    return x-y

@debug(prefix = "i am calling: ")
def mul(x,y):
    return x*y

@debug(prefix="I am Calling: ")
def div(x,y):
    return x/y


div(49,7)
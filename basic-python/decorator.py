import time
# We import this so that the decorators won't swallow the function's metadata
from functools import wraps


# We define a function that will work as our decorator
def double_args(func):
    # For this, we define a wrapper for the function that we will be decorating. We define any logic that will modify
    # the call to the function
    @wraps(func)
    def wrapper(a, b):
        return func(a * 2, b * 2)

    # and return that wrapper
    return wrapper


# when we define our wrapper-returning method, we can reference is with the @ symbol and the method name
@double_args
def multiply(a, b):
    return a * b


# Using the @ symbol is equivalent to overwriting the method, e.g:
# multiply = double_args(multiply)
print(multiply(1, 5))


# USEFUL DECORATORS:
# Defining a timer decorator for any function:
def timer(func):
    """ Measures execution time of decorated function """
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_total = time.time() - t_start

        print("{} took {}s.".format(func.__name__, t_total))
        return result

    return wrapper


@timer
def sleep_test():
    time.sleep(5)


sleep_test()


# Defining a caching decorator:
def cacheable(func):
    """ Stores result of decorated function in a cache """
    cache = {}

    def wrapper(*args, **kwargs):
        if (args, kwargs) not in cache:  # unhashable type: dict
            cache[(args, kwargs)] = func(*args, **kwargs)

        return cache[(args, kwargs)]

    return wrapper


@cacheable
def slow_function(a, b):
    print("Sleeping")
    time.sleep(5)
    return a + b


slow_function(1, 2)
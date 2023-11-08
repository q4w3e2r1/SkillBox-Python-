import time


def timer(func):

    def wrapped_func(*args):
        start = time.time()

        value = func(*args)
        end = time.time()
        run_time = round(end - start, 10)
        print(f"Функция отработала за: {run_time}")

        return value

    wrapped_func.__name__ = func.__name__
    wrapped_func.__doc__ = func.__doc__
    return wrapped_func


def validate_args(func):
    def wrapped_func(*args):
        if len(args) < 1:
            return "Not enough arguments"
        if len(args) > 1:
            return "Too many arguments"
        if not isinstance(args[0], int):
            return "Wrong types"
        if args[0] < 0:
            return "Negative argument"

        value = func(*args)
        return value

    wrapped_func.__name__ = func.__name__
    wrapped_func.__doc__ = func.__doc__
    return wrapped_func


def memoize(func):
    cache = {}

    def wrapped_func(*args):
        key = args
        if key in cache:
            return cache[key]
        value = func(*args)
        cache[args] = value
        return value

    wrapped_func.__name__ = func.__name__
    wrapped_func.__doc__ = func.__doc__

    return wrapped_func


@validate_args
@memoize
def fibonacci(n):
    """Это функция, котороя принимает позицию числа фибоначи и возвращает это число"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibo = timer(fibonacci)
print(fibo(250))


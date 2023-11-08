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

    return wrapped_func

@validate_args
def func(a):
    return a


print(func(-1))
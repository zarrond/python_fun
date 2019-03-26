from debug_tools import dprint


def catch_exception(func):
    dprint("re")

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return True,e
    return wrapper


@catch_exception
def bad_func(do_mistake):
    if do_mistake:
        return print(4/0)
    return print(4)


# bad_func(False)
print(bad_func(False))

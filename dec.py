def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function', func.__name__)
        print('positional argument', args)
        print('Keyword arguments', kwargs)
        result = func(*args, **kwargs)
        print("result:", result)
        return result
    return new_function


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)

        return result*result

    return new_function


@document_it
@square_it
def add_ints(a, b):
    return a+b


add_ints(3, 5)

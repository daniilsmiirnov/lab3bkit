def print_result(func):
    def dec_func(*args):
        print(func.__name__)
        result = func(*args)
        print(result)
        return result
    return dec_func


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]
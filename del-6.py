def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class MyException(Exception):
    pass

def subgen():
    while True:
        try:
            message = yield
        except MyException:
            print("smth")
        else:
            print("...........", message)

@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except StopIteration:
    #         pass
    #     else:
    #         print("...........", message)
    yield from g
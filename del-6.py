def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class MyException():
    pass


def subgen():
    for i in "oleg":
        yield i

def delegator(g):
    for i in g:
        yield i
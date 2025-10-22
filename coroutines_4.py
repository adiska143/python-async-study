def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


@coroutine
def average():
    count = 0
    summ = 0
    avg = None

    while True:
        try:
            x = yield avg
        except StopIteration:
            print("done")
        else:
            count += 1
            summ += x
            avg = round(summ / count, 2)


g = average()
g.send(12)
g.send(16)
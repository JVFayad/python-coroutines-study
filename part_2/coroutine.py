
def coroutine(func):
    def preparation(*args, **kwargs):
        coro = func(*args, **kwargs)
        next(coro)
        return coro
    return preparation
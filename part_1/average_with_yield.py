from coroutine import coroutine


@coroutine
def media():
    total = 0.0
    contador = 0
    media = 'Vamos calcular a média!'
    while True:
        entrada = yield media
        total += entrada
        contador += 1
        media = total/contador


coro = media()

# preparação necessária, mas já estamos fazendo isso no decorator coroutine
# next(coro)  

coro.send(10)  # 10.0
coro.send(20)  # 15.0

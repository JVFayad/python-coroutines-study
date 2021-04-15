from coroutine import coroutine


@coroutine
def print_(formatacao):
    while True:
        values = yield
        print(formatacao.format(*values))


@coroutine
def media(target):
    total = 0.0
    contador = 0
    while True:
        contador += 1
        total += yield
        target.send(
            (contador, total, total/contador)
        )


formatacao = print_(
    'Contador: {} - Total: {} - Resultado: {}'
)

# formatação = print_(
#     'A: {} - B: {} - C: {}'
# )

coro = media(target=formatacao)
coro.send(10)  # Contador: 1 - Total: 10.0 - Resultado: 10.0
coro.send(20)  # Contador: 2 - Total: 30.0 - Resultado: 15.0
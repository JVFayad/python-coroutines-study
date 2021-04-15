from coroutine import coroutine


@coroutine
def print_(formatação):
    while True:
        values = yield
        print(formatação.format(*values))


@coroutine
def grep(target, pattern):
    while True:
        item = yield
        if pattern in item:
            target.send(item)


@coroutine
def replace(search, replace, *, target):
    while True:
        target.send(
            (search, replace, (yield).replace(search, replace))
        )


@coroutine
def dividir(*targets):
    while True:
        item = yield
        for target in targets:
            target.send(item)


printer = print_('Entrada: {} - Replace: {} - Valor final: {}')

replacer_spam = replace(  # troca spam por bacon
    search='spam', replace='bacon', target=printer
)

replacer_spam_spam = replace(  # troca 'spam spam' por eggs
    search='spam spam', replace='eggs', target=printer
)

branch = dividir(replacer_spam, replacer_spam_spam)


grepper = grep(branch, 'spam')  # Filtra por spam

dados = ['spam', 'spam spam', 'eggs']

for line in dados:
    grepper.send(line)
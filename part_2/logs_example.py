from coroutine import coroutine
from collections import namedtuple

log_line = namedtuple('Log', 'data ampm bool nome telefone email')


@coroutine
def re_type():
    types = [str, str, eval, str, str, str]
    value = None
    while True:
        unformated = yield value
        value = [f(d) for f, d in zip(types, unformated)]


@coroutine
def convert_to_tuple():
    data = None
    while True:
        value = yield data
        data = log_line(*retype.send(value.split(',')))


@coroutine
def grep(pattern, target):
    for line in target:
        if pattern in line:
            yield tr.send(line)


@coroutine
def filter_bool(target):
    for log in target:
        if log.bool:
            yield log


logs = open('part_2/logs.csv')

tr = convert_to_tuple()
retype = re_type()

a = grep('AM', logs)
b = filter_bool(a)

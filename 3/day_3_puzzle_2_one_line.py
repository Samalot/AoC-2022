import Reader
from functools import reduce


def priority(char):
    p = ord(char) - 96
    return p if p > 0 else p + 58


def run():
    return sum(map(lambda a: priority(a.pop()), map(lambda a: reduce(lambda b, c: b.intersection(c), a), zip(*(iter(map(lambda a: set(list(a)), [*Reader.read("input")])),) * 3))))


print(f'Answer: {run()}')

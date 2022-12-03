import Reader
from functools import reduce


def priority(char):
    p = ord(char) - 96
    return p if p > 0 else p + 58


def run():
    sets = map(lambda a: set(list(a)), [*Reader.read("input")])
    groups = zip(*(iter(sets),) * 3)
    intersections = map(lambda a: reduce(lambda b, c: b.intersection(c), a), groups)
    priorities = map(lambda a: priority(a.pop()), intersections)
    return sum(priorities)


print(f'Answer: {run()}')

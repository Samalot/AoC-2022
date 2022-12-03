import Reader


def run():
    return sum(list(map(lambda a: (ord(a) - 96) if (ord(a) - 96) > 0 else (ord(a) - 96) + 58, map(lambda a: a[0].intersection(a[1]).intersection(a[2]).pop(), map(lambda a: list(map(lambda b: set(list(b[1])), a)), zip(filter(lambda a: (a[0] % 3) == 0, enumerate([line for line in Reader.read("input")])), filter(lambda a: (a[0] % 3) == 1, enumerate([line for line in Reader.read("input")])), filter(lambda a: (a[0] % 3) == 2, enumerate([line for line in Reader.read("input")]))))))))


print(f'Answer: {run()}')

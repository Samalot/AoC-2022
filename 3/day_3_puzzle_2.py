import Reader


def priority(char):
    p = ord(char) - 96
    return p if p > 0 else p + 58


def run():
    total = 0
    group = [set([]), set([]), set([])]

    for index, line in enumerate(Reader.read("input")):

        group_index = index % 3
        group[group_index] = set(list(line))

        if group_index == 2:
            badge = group[0].intersection(group[1]).intersection(group[2]).pop()
            total += priority(badge)

    return total


print(f'Answer: {run()}')


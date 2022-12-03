import Reader


def priority(char):
    p = ord(char) - 96
    return p if p > 0 else p + 58


def run():
    total = 0
    for line in Reader.read("input"):
        length = len(line) // 2
        first_compartment = set(list(line[0:length]))
        second_compartment = set(list(line[length: len(line)]))
        letter_in_both = first_compartment.intersection(second_compartment).pop()
        total += priority(letter_in_both)
    return total


print(f'Answer: {run()}')


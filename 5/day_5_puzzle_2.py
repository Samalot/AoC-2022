import Reader
import re

stacks = [
    ['R', 'G', 'H', 'Q', 'S', 'B', 'T', 'N'],
    ['H', 'S', 'F', 'D', 'P', 'Z', 'J'],
    ['Z', 'H', 'V'],
    ['M', 'Z', 'J', 'F', 'G', 'H'],

    ['T', 'Z', 'C', 'D', 'L', 'M', 'S', 'R'],
    ['M', 'T', 'W', 'V', 'H', 'Z', 'J'],
    ['T', 'F', 'P', 'L', 'Z'],
    ['Q', 'V', 'W', 'S'],
    ['W', 'H', 'L', 'M', 'T', 'D', 'N', 'C']
]


def run():
    for instruction in Reader.read("input"):
        m = re.match(r'move (?P<amount>.*) from (?P<start>.*) to (?P<end>.*)', instruction)
        amount, start, end = map(int, m.groups())

        stacks[end - 1] += stacks[start - 1][len(stacks[start - 1]) - amount:]
        stacks[start - 1] = stacks[start - 1][:len(stacks[start - 1]) - amount]

    return ''.join([stack[-1] for stack in stacks])


print(f'Answer: {run()}')


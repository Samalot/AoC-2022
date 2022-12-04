import Reader
import re


def run():
    total = 0
    for pair in Reader.read("input"):
        a_start, a_end, b_start, b_end, = map(lambda x: int(x), re.split('-|,', pair))

        if a_start <= b_start <= a_end or a_start <= b_end <= a_end or b_start <= a_start <= b_end or b_start <= a_end <= b_end:
            total += 1

    return total


print(f'Answer: {run()}')

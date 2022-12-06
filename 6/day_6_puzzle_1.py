import Reader


def run():
    for buffer in Reader.read("input"):
        for index in range(len(buffer)):
            if index > 2 and len(set([buffer[index - (3 - x)] for x in range(4)])) == 4:
                return index + 1
    return 0


print(f'Answer: {run()}')


import Reader


def run():
    for buffer in Reader.read("input"):
        size, total, counts = 14, 0, {}

        for index in range(len(buffer)):
            if index >= size:
                counts[buffer[index - size]] -= 1
                if counts[buffer[index - size]] == 0:
                    total -= 1

            if index >= (size - 1):
                counts[buffer[index]] = counts.get(buffer[index], 0) + 1
                if counts[buffer[index]] == 1:
                    total += 1

            elif not buffer[index] in counts:
                counts[buffer[index]] = 1
                total += 1
            else:
                counts[buffer[index]] += 1

            if total == size:
                return index + 1

    return 0


print(f'Answer: {run()}')


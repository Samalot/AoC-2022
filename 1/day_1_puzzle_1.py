import Reader


def run():
    elves = [0]
    for data in Reader.read("input"):
        if data.isdigit():
            elves[-1] += int(data)
        else:
            elves.append(0)

    return max(elves)


print(f'Answer: {run()}')

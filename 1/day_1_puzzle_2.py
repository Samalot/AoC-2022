import Reader


def run():
    elves = [0]
    for data in Reader.read("input"):
        if data.isdigit():
            elves[-1] += int(data)
        else:
            elves.append(0)

    return sum(sorted(elves, reverse=True)[0:3])


print(f'Answer: {run()}')


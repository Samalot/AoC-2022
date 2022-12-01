import Reader


def run():
    elves = [0]
    for line in Reader.read("input"):
        if line.isdigit():
            elves[-1] += int(line)
        else:
            elves.append(0)

    return sum(sorted(elves, reverse=True)[0:3])


print(f'Answer: {run()}')


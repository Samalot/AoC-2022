import Reader


def move_pair(start, end):
    if abs(start[0] - end[0]) > 1 or abs(start[1] - end[1]) > 1:
        if start[1] == end[1]:
            end[0] += 1 if (start[0] > end[0]) else -1

        elif start[0] == end[0]:
            end[1] += 1 if (start[1] > end[1]) else -1

        else:
            end[0] += 1 if (start[0] > end[0]) else -1
            end[1] += 1 if (start[1] > end[1]) else -1

    return start, end


def run():
    positions = [[0, 0] for i in range(10)]
    tail_visited = set([(0, 0)])
    modifiers = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

    for line in Reader.read("input"):
        direction, amount = line.split(' ')
        for i in range(int(amount)):
            positions[0][0] += modifiers[direction][0]
            positions[0][1] += modifiers[direction][1]

            for i in range(1, len(positions)):
                positions[i-1], positions[i] = move_pair(positions[i-1], positions[i])

            tail_visited.add((positions[-1][0], positions[-1][1]))

    return len(tail_visited)


print(f'Answer: {run()}')


import Reader


def run():
    head_pos, tail_pos = [0, 0], [0, 0]

    tail_visited = set([(0, 0)])
    modifiers = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

    for line in Reader.read("input"):
        direction, amount = line.split(' ')
        for i in range(int(amount)):
            head_pos[0] += modifiers[direction][0]
            head_pos[1] += modifiers[direction][1]

            if abs(head_pos[0] - tail_pos[0]) > 1 or abs(head_pos[1] - tail_pos[1]) > 1:
                if head_pos[1] == tail_pos[1]:
                    tail_pos[0] += 1 if (head_pos[0] > tail_pos[0]) else -1

                elif head_pos[0] == tail_pos[0]:
                    tail_pos[1] += 1 if (head_pos[1] > tail_pos[1]) else -1

                else:
                    tail_pos[0] += 1 if (head_pos[0] > tail_pos[0]) else -1
                    tail_pos[1] += 1 if (head_pos[1] > tail_pos[1]) else -1

                tail_visited.add((tail_pos[0], tail_pos[1]))

    return len(tail_visited)


print(f'Answer: {run()}')


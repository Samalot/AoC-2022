import Reader


def run():
    crt_width = 40
    crt_height = 6
    register = 1
    instructions = []
    for line in Reader.read("input"):
        if line == "noop":
            instructions.append([1, 0])
        else:
            instructions.append([2, int(line.split(" ")[1])])

    display = [['.' for x in range(crt_width)] for y in range(crt_height)]
    for row in range(crt_height):
        for col in range(0, crt_width):

            if abs(col - register) <= 1 or (col - register == crt_width - 1):
                display[row][col] = '#'

            if instructions[0][0] == 1:
                register += instructions[0][1]
                instructions.pop(0)
            else:
                instructions[0][0] -= 1

    for row in display:
        print(''.join(row))




run()


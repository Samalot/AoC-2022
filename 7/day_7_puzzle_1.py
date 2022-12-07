import Reader


def run():
    dir_size_builder, dir_size = [], []
    for command in Reader.read("input"):
        if command[0] == "$":
            if command[5:7] == "..":
                dir_size.append(dir_size_builder.pop())
                dir_size_builder[-1] += dir_size[-1]

            elif command[2] == "c":
                dir_size_builder.append(0)

        elif not command[:3] == "dir":
            dir_size_builder[-1] += int(command.split(" ")[0])

    for i in range(1, len(dir_size_builder)):
        dir_size.append(dir_size_builder.pop())
        dir_size_builder[-1] += dir_size[-1]

    return sum(filter(lambda x: x <= 100000, dir_size))


print(f'Answer: {run()}')


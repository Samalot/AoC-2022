import Reader


def run():
    dir_size_builder, dir_size = [], []
    for command in Reader.read("input"):
        if command[0] == "$":
            # If "Move up" then remove directory from builder and add it's size to parent
            if command[5:7] == "..":
                dir_size.append(dir_size_builder.pop())
                dir_size_builder[-1] += dir_size[-1]

            # If "New Directory" then add new count to the builder stack
            elif command[2] == "c":
                dir_size_builder.append(0)

        # If File - add it's size to the last element in the builder Stack
        elif not command[:3] == "dir":
            dir_size_builder[-1] += int(command.split(" ")[0])

    # Add the remaining directories to the finished array
    for i in range(1, len(dir_size_builder)):
        dir_size.append(dir_size_builder.pop())
        dir_size_builder[-1] += dir_size[-1]

    dir_size = sorted(dir_size + dir_size_builder)
    space_needed = 30000000 - (70000000 - dir_size_builder[0])

    return list(filter(lambda x: x >= space_needed, dir_size))[0]


print(f'Answer: {run()}')


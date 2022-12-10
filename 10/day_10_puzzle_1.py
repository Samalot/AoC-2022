import Reader


def run():
    register = 1
    cycle = 0
    target = 20
    cycle_values = []
    for line in Reader.read("input"):
        modifier_register = 0
        modifier_cycle = 1

        if not line == "noop":
            modifier_cycle = 2
            modifier_register = int(line.split(" ")[1])

        cycle += modifier_cycle
        if cycle >= target:
            cycle_values.append(register * target)
            target += 40

        register += modifier_register
    return sum(cycle_values)


print(f'Answer: {run()}')


import Reader


def process(grid, init_max, iterator):
    visible = set([])
    max_height = init_max
    for (x, y) in iterator:
        if grid[y][x] > max_height:
            max_height = grid[y][x]
            visible.add((x, y))
    return visible


def run():
    visible = set([])
    grid = []
    for tree_line in Reader.read("input"):
        grid.append(list(map(int, list(tree_line))))

    for y in range(1, len(grid) - 1):
        visible = visible.union(process(grid, grid[y][0], [(x, y) for x in range(1, len(grid[0]) - 1, 1)]))
        visible = visible.union(process(grid, grid[y][-1], [(x, y) for x in range(len(grid[0]) - 2, 0, -1)]))

    for x in range(1, len(grid[0]) - 1):
        visible = visible.union(process(grid, grid[0][x], [(x, y) for y in range(1, len(grid) - 1, 1)]))
        visible = visible.union(process(grid, grid[-1][x], [(x, y) for y in range(len(grid) - 2, 0, -1)]))

    perimeter_size = len(grid) * 2 + (len(grid[0]) - 2) * 2
    return len(visible) + perimeter_size


print(f'Answer: {run()}')


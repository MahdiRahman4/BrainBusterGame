def build_grid(commandLineInput):
    grid = [[0] * commandLineInput for _ in range(commandLineInput)]
    return grid
def print_grid(grid):
    for row in grid:
        print(row)
def build_grid(commandLineInput):
    grid = [[0] * commandLineInput for _ in range(commandLineInput)]
    for row in grid:
        print(row)
    
    return grid
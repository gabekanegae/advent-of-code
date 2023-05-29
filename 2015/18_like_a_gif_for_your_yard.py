############################################
# --- Day 18: Like a GIF For Your Yard --- #
############################################

import AOCUtils

def step(grid, part=1):
    size_x, size_y = len(grid), len(grid[0])

    if part == 2:
        grid[0][0] = '#'
        grid[size_x-1][0] = '#'
        grid[0][size_y-1] = '#'
        grid[size_x-1][size_y-1] = '#'

    new_grid = [row[:] for row in grid]

    for i in range(size_x):
        for j in range(size_y):
            if part == 2 and i in [0, size_x-1] and j in [0, size_y-1]: continue

            neighbors = 0

            if i-1 >= 0 and j-1 >= 0:
                neighbors += int(grid[i-1][j-1] == '#')
            if i-1 >= 0:
                neighbors += int(grid[i-1][j] == '#')
            if i-1 >= 0 and j+1 < size_y:
                neighbors += int(grid[i-1][j+1] == '#')

            if j-1 >= 0:
                neighbors += int(grid[i][j-1] == '#')
            if j+1 < size_y:
                neighbors += int(grid[i][j+1] == '#')

            if i+1 < size_x and j-1 >= 0:
                neighbors += int(grid[i+1][j-1] == '#')
            if i+1 < size_x:
                neighbors += int(grid[i+1][j] == '#')
            if i+1 < size_x and j+1 < size_y:
                neighbors += int(grid[i+1][j+1] == '#')

            if grid[i][j] == '#':
                new_grid[i][j] = '#' if neighbors in [2, 3] else '.'
            elif grid[i][j] == '.':
                new_grid[i][j] = '#' if neighbors == 3 else '.'

    return new_grid

############################################

start_grid = [list(s) for s in AOCUtils.load_input(18)]

grid = [row[:] for row in start_grid]
for _ in range(100):
    grid = step(grid, part=1)

AOCUtils.print_answer(1, sum(row.count('#') for row in grid))

grid = [row[:] for row in start_grid]
for _ in range(100):
    grid = step(grid, part=2)

AOCUtils.print_answer(2, sum(row.count('#') for row in grid))

AOCUtils.print_time_taken()
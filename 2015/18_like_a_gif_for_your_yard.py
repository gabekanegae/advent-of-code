############################################
# --- Day 18: Like a GIF For Your Yard --- #
############################################

import AOCUtils

def step(grid, part=1):
    sizeX, sizeY = len(grid), len(grid[0])

    if part == 2:
        grid[0][0] = "#"
        grid[sizeX-1][0] = "#"
        grid[0][sizeY-1] = "#"
        grid[sizeX-1][sizeY-1] = "#"

    newGrid = [row[:] for row in grid]

    for i in range(sizeX):
        for j in range(sizeY):
            if part == 2 and i in [0, sizeX-1] and j in [0, sizeY-1]: continue

            neighbors = 0

            if i-1 >= 0 and j-1 >= 0:
                neighbors += int(grid[i-1][j-1] == "#")
            if i-1 >= 0:
                neighbors += int(grid[i-1][j] == "#")
            if i-1 >= 0 and j+1 < sizeY:
                neighbors += int(grid[i-1][j+1] == "#")

            if j-1 >= 0:
                neighbors += int(grid[i][j-1] == "#")
            if j+1 < sizeY:
                neighbors += int(grid[i][j+1] == "#")

            if i+1 < sizeX and j-1 >= 0:
                neighbors += int(grid[i+1][j-1] == "#")
            if i+1 < sizeX:
                neighbors += int(grid[i+1][j] == "#")
            if i+1 < sizeX and j+1 < sizeY:
                neighbors += int(grid[i+1][j+1] == "#")

            if grid[i][j] == "#":
                newGrid[i][j] = "#" if neighbors in [2, 3] else "."
            elif grid[i][j] == ".":
                newGrid[i][j] = "#" if neighbors == 3 else "."

    return newGrid

############################################

startGrid = [list(s) for s in AOCUtils.loadInput(18)]

grid = [row[:] for row in startGrid]
for _ in range(100):
    grid = step(grid, part=1)

print("Part 1: {}".format(sum(row.count("#") for row in grid)))

grid = [row[:] for row in startGrid]
for _ in range(100):
    grid = step(grid, part=2)

print("Part 2: {}".format(sum(row.count("#") for row in grid)))

AOCUtils.printTimeTaken()
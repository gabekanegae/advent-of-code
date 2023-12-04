######################################
# --- Day 6: Chronal Coordinates --- #
######################################

import AOCUtils

def get_distance(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

def get_all_distances(p, coords):
    return [get_distance(p, c) for c in coords]

######################################

raw_coords = AOCUtils.load_input(6)

grid_size_x, grid_size_y = 0, 0
coords = []
for i in raw_coords:
    x, y = map(int, i.split(', '))
    coords.append((x, y))

    if x > grid_size_x: grid_size_x = x
    if y > grid_size_y: grid_size_y = y

grid_size_x += 1
grid_size_y += 1

distances = [[get_all_distances((i, j), coords) for j in range(grid_size_y)] for i in range(grid_size_x)]

grid = [[None for _ in range(grid_size_y)] for _ in range(grid_size_x)]
for i in range(grid_size_x):
    for j in range(grid_size_y):
        min_distance = min(distances[i][j])
        if distances[i][j].count(min_distance) <= 1:
            grid[i][j] = distances[i][j].index(min_distance)

areas = [0 for _ in range(len(coords))]
for i in range(grid_size_x):
    for j in range(grid_size_y):
        if grid[i][j]: areas[grid[i][j]] += 1

for i in range(grid_size_x):
    if grid[i][0]: areas[grid[i][0]] = 0
    if grid[i][-1]: areas[grid[i][-1]] = 0

for i in range(grid_size_y):
    if grid[0][i]: areas[grid[0][i]] = 0
    if grid[-1][i]: areas[grid[-1][i]] = 0

AOCUtils.print_answer(1, max(areas))

count = 0
for i in range(grid_size_x):
    for j in range(grid_size_y):
        if sum(distances[i][j]) < 10000:
            count += 1

AOCUtils.print_answer(2, count)

AOCUtils.print_time_taken()
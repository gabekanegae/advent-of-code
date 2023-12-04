#####################################
# --- Day 24: Planet of Discord --- #
#####################################

import AOCUtils

#####################################

raw_layout = AOCUtils.load_input(24)
layout = list(map(list, raw_layout))

size = (len(layout), len(layout[0]))

seen = set()
while True:
    # Calculate biodiversity rating
    bio_rating = 0
    for x in range(size[0]):
        for y in range(size[1]):
            if layout[x][y] == '#':
                bio_rating += 2 ** (x*size[1] + y)

    if bio_rating in seen: break
    seen.add(bio_rating)
    
    # Update layout
    new_layout = [s[:] for s in layout]
    for x in range(size[0]):
        for y in range(size[1]):
            alive_neighbors = 0
            if x-1 >= 0 and layout[x-1][y] == '#': alive_neighbors += 1
            if y-1 >= 0 and layout[x][y-1] == '#': alive_neighbors += 1
            if x+1 < size[0] and layout[x+1][y] == '#': alive_neighbors += 1
            if y+1 < size[1] and layout[x][y+1] == '#': alive_neighbors += 1

            if layout[x][y] == '#' and alive_neighbors != 1:
                new_layout[x][y] = '.'
            elif layout[x][y] == '.' and alive_neighbors in [1, 2]:
                new_layout[x][y] = '#'
    layout = new_layout

AOCUtils.print_answer(1, bio_rating)

# Each iteration will spread bugs to, at most, +1 upper and +1 lower level
iterations = 200
levels = iterations // 2

# Convert list of lists to dict
layout = dict()
for x in range(size[0]):
    for y in range(size[1]):
        for level in range(-levels, levels+1):
            if (x, y) == (2, 2): continue

            if level == 0: layout[(x, y, 0)] = raw_layout[x][y]
            else: layout[(x, y, level)] = '.'

# Generate list of neighbors for each position
neighbors = dict()
for x in range(size[0]):
    for y in range(size[1]):
        if (x, y) == (2, 2): continue

        for level in range(-levels, levels+1):
            this_neighbors = []

            # Same level
            for m in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                xi, yi = x+m[0], y+m[1]
                if 0 <= xi < size[0] and 0 <= yi < size[1] and (xi, yi) != (2, 2):
                    this_neighbors.append((xi, yi, level))

            # Lower level
            if level-1 >= -levels:
                if x == 0: this_neighbors.append((1, 2, level-1))
                if y == 0: this_neighbors.append((2, 1, level-1))
                if x == size[0]-1: this_neighbors.append((3, 2, level-1))
                if y == size[1]-1: this_neighbors.append((2, 3, level-1))

            # Upper level
            if level+1 <= levels:
                if (x, y) == (1, 2): this_neighbors += [(0, yi, level+1) for yi in range(size[1])]
                if (x, y) == (2, 1): this_neighbors += [(xi, 0, level+1) for xi in range(size[0])]
                if (x, y) == (3, 2): this_neighbors += [(size[0]-1, yi, level+1) for yi in range(size[1])]
                if (x, y) == (2, 3): this_neighbors += [(xi, size[1]-1, level+1) for xi in range(size[0])]

            neighbors[(x, y, level)] = this_neighbors

# Run all iterations
for i in range(iterations):
    new_layout = dict()
    for k, v in layout.items():
        alive_neighbors = sum(layout[neighbor] == '#' for neighbor in neighbors[k])

        if v == '#' and alive_neighbors != 1:
            new_layout[k] = '.'
        elif v == '.' and alive_neighbors in [1, 2]:
            new_layout[k] = '#'
        else:
            new_layout[k] = layout[k]

    layout = new_layout

bugs_count = sum(v == '#' for v in layout.values())
AOCUtils.print_answer(2, bugs_count)

AOCUtils.print_time_taken()